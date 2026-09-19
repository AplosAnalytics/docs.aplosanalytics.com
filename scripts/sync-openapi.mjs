#!/usr/bin/env node
/**
 * Sync the docs site's API reference data from the generated OpenAPI spec.
 *
 * The OpenAPI spec is the single source of truth. It is generated in the
 * Aplos-NCA-SaaS-IaC repo from the Lambda config JSONs and published to the
 * OpenAPI docs site (openapi.<zone>.aplos-nca.com/openapi-spec.json).
 *
 * This script (docs *pulls*, IaC does not *push*):
 *   1. Fetches that published spec (URL configurable via OPENAPI_SPEC_URL) and
 *      writes it verbatim to docs/api/openapi-spec.json.
 *   2. Transforms it into docs/api/endpoints/routes.json — the data the
 *      existing DisplayRoutes.vue table renders — so the routes page always
 *      reflects the real, current API surface.
 *
 * Design notes:
 *   - Node-only (uses global fetch, Node 18+). No new runtime dependency, so it
 *     runs in the existing VitePress CI build with nothing extra installed.
 *   - Network-tolerant: if the fetch fails (offline dev, transient CI error)
 *     AND a previously-synced spec exists on disk, we fall back to it and still
 *     regenerate routes.json. Only a hard failure with no cached spec is fatal,
 *     and even then it is downgraded to a warning unless STRICT=1 (so a docs
 *     build is never blocked by a docs-unrelated network blip). CI can set
 *     STRICT=1 to require a fresh pull.
 *   - Both outputs are committed to the repo so the public repo shows current
 *     data without requiring a network fetch to view it.
 *
 * Usage:
 *   node scripts/sync-openapi.mjs
 *   OPENAPI_SPEC_URL=https://openapi.dev.aplos-nca.com/openapi-spec.json node scripts/sync-openapi.mjs
 *   OPENAPI_SPEC_URL=../Aplos-NCA-SaaS-IaC/cdk/.dynamic/api-docs/openapi-spec.json node scripts/sync-openapi.mjs
 *   STRICT=1 node scripts/sync-openapi.mjs   # fail the build if the fetch fails
 *
 * OPENAPI_SPEC_URL accepts an http(s) URL, a file:// URL, or a plain local path.
 */

import { promises as fs } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, "..");

const SPEC_URL =
  process.env.OPENAPI_SPEC_URL ||
  "https://openapi.dev.aplos-nca.com/openapi-spec.json";
const STRICT = process.env.STRICT === "1" || process.env.STRICT === "true";

const SPEC_OUT = path.join(REPO_ROOT, "docs", "api", "openapi-spec.json");
const ROUTES_OUT = path.join(
  REPO_ROOT,
  "docs",
  "api",
  "endpoints",
  "routes.json"
);

const METHOD_ORDER = ["get", "post", "put", "patch", "delete"];

/**
 * Fetch the spec JSON from SPEC_URL, or return null on any failure.
 *
 * Supports http(s) URLs (via fetch) as well as a local source: either a
 * `file://` URL or a plain filesystem path. The local form lets CI point at a
 * spec produced by a co-checked-out IaC repo instead of the network.
 */
async function fetchSpec(url) {
  const isHttp = /^https?:\/\//i.test(url);
  if (!isHttp) {
    const localPath = url.startsWith("file://") ? fileURLToPath(url) : url;
    try {
      return JSON.parse(await fs.readFile(localPath, "utf8"));
    } catch (err) {
      console.warn(`  local read failed for ${localPath}: ${err.message}`);
      return null;
    }
  }
  try {
    const res = await fetch(url, { redirect: "follow" });
    if (!res.ok) {
      console.warn(`  fetch returned HTTP ${res.status} for ${url}`);
      return null;
    }
    return await res.json();
  } catch (err) {
    console.warn(`  fetch failed for ${url}: ${err.message}`);
    return null;
  }
}

/** Read a previously-synced spec from disk, or return null if absent/invalid. */
async function readCachedSpec(file) {
  try {
    return JSON.parse(await fs.readFile(file, "utf8"));
  } catch {
    return null;
  }
}

/**
 * Build a stable id for a route from its operationId (already unique per
 * operation in the spec). Falls back to a method+path slug.
 */
function routeId(operation, method, routePath) {
  const opId = operation.operationId;
  if (opId) return opId;
  const slug = routePath.replace(/[^A-Za-z0-9]+/g, "-").replace(/^-|-$/g, "");
  return `${method}-${slug}`.toLowerCase();
}

/**
 * Transform the OpenAPI document into the routes.json shape consumed by
 * DisplayRoutes.vue: { routes: [{ id, name, path, method_type, description,
 * auth, tag }] }.
 *
 * - name comes from x-display-name (the friendly name set via api.display_name
 *   in the IaC config), falling back to operationId.
 * - path is the server URL + the route template, with the {tenant} host segment
 *   preserved as a readable placeholder.
 * - description comes from the operation summary.
 * - auth is false for public operations (security: []), true otherwise.
 */
function specToRoutes(spec) {
  // Prefer a tenant-templated host so the docs read generically rather than
  // pinning to whatever environment generated the spec (e.g. api.dev...).
  const rawServer =
    (spec.servers && spec.servers[0] && spec.servers[0].url) ||
    "https://api.<tenant>.aplos-nca.com";
  const host = rawServer.replace(
    /^https:\/\/api\.[^/]+/,
    "https://api.<tenant>.aplos-nca.com"
  );

  const routes = [];
  for (const [routePath, methods] of Object.entries(spec.paths || {})) {
    const present = Object.keys(methods).filter((m) =>
      METHOD_ORDER.includes(m.toLowerCase())
    );
    present.sort(
      (a, b) =>
        METHOD_ORDER.indexOf(a.toLowerCase()) -
        METHOD_ORDER.indexOf(b.toLowerCase())
    );
    for (const method of present) {
      const op = methods[method];
      const isPublic = Array.isArray(op.security) && op.security.length === 0;
      routes.push({
        id: routeId(op, method, routePath),
        name: op["x-display-name"] || op.operationId || `${method.toUpperCase()} ${routePath}`,
        path: `${host}${routePath}`,
        method_type: method.toUpperCase(),
        description: op.summary || "",
        auth: !isPublic,
        tag: (op.tags && op.tags[0]) || "",
      });
    }
  }

  // Group by tag, then by name, for a stable, readable ordering.
  routes.sort((a, b) => {
    if (a.tag !== b.tag) return a.tag.localeCompare(b.tag);
    return a.name.localeCompare(b.name);
  });

  return { routes };
}

async function main() {
  console.log("Syncing OpenAPI spec for docs...");
  console.log(`  source: ${SPEC_URL}`);

  let spec = await fetchSpec(SPEC_URL);
  let fromCache = false;

  if (spec) {
    await fs.mkdir(path.dirname(SPEC_OUT), { recursive: true });
    await fs.writeFile(SPEC_OUT, JSON.stringify(spec, null, 2) + "\n", "utf8");
    console.log(`  wrote spec -> ${path.relative(REPO_ROOT, SPEC_OUT)}`);
  } else {
    spec = await readCachedSpec(SPEC_OUT);
    fromCache = spec !== null;
    if (fromCache) {
      console.warn(
        `  using previously-synced spec at ${path.relative(REPO_ROOT, SPEC_OUT)}`
      );
    }
  }

  if (!spec) {
    const msg =
      "No OpenAPI spec available (fetch failed and no cached copy on disk).";
    if (STRICT) {
      console.error(`ERROR: ${msg}`);
      process.exit(1);
    }
    console.warn(`WARNING: ${msg} Skipping routes regeneration.`);
    return;
  }

  if (fromCache && STRICT) {
    console.error("ERROR: STRICT mode requires a fresh spec fetch, but it failed.");
    process.exit(1);
  }

  const routesDoc = specToRoutes(spec);
  await fs.mkdir(path.dirname(ROUTES_OUT), { recursive: true });
  await fs.writeFile(
    ROUTES_OUT,
    JSON.stringify(routesDoc, null, 4) + "\n",
    "utf8"
  );
  console.log(
    `  wrote ${routesDoc.routes.length} routes -> ${path.relative(
      REPO_ROOT,
      ROUTES_OUT
    )}`
  );
  console.log("Done.");
}

main().catch((err) => {
  // A docs build should not hard-fail on a docs-unrelated sync error unless
  // STRICT is set. Surface the error and exit non-zero only in strict mode.
  console.error(`sync-openapi failed: ${err.stack || err.message}`);
  process.exit(STRICT ? 1 : 0);
});

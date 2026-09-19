<script setup>
import { computed } from "vue";
import data from "/docs/api/endpoints/routes.json";
import { defineProps } from "vue";

const props = defineProps({
  // Match against a route's stable id OR any of its aliases (operationId +
  // doc alias), so references keep working across operationId changes.
  routeId: {
    type: Array,
    default: () => [],
  },
  // Optional: restrict to routes in a single tag/group.
  tag: {
    type: String,
    default: "",
  },
  // Columns for the compact table layout. Ignored by the other layouts.
  columnsToShow: {
    type: Array,
    default: () => ["name", "method_type", "path"],
  },
  // Layout:
  //   "auto"     - stacked card for a single route, compact table otherwise
  //   "sections" - group by feature area (tag): H2 section + H3 per route +
  //                a property/value table (Method / Endpoint URL / Auth)
  //   "detailed" - always the stacked card
  //   "table"    - always the compact table
  layout: {
    type: String,
    default: "auto",
  },
});

const columnLabels = {
  name: "Route Name",
  path: "Endpoint URL",
  description: "Description",
  method_type: "Method",
  auth: "Auth",
  tag: "Group",
};

function matches(route, wanted) {
  if (route.id === wanted) return true;
  return Array.isArray(route.aliases) && route.aliases.includes(wanted);
}

const endpoints = computed(() => {
  let routes = data.routes;
  if (props.routeId.length > 0) {
    routes = routes.filter((route) =>
      props.routeId.some((w) => matches(route, w))
    );
  }
  if (props.tag) {
    routes = routes.filter((route) => route.tag === props.tag);
  }
  return routes;
});

// Resolve the effective layout. "auto" picks the stacked card for a single
// route (the executions pages) and the compact table otherwise.
const resolvedLayout = computed(() => {
  if (props.layout && props.layout !== "auto") return props.layout;
  return endpoints.value.length === 1 ? "detailed" : "table";
});

// Turn a tag slug ("file-system") into a section title ("File System").
function titleCase(tag) {
  if (!tag) return "Other";
  return tag
    .split(/[-_]/)
    .map((w) => w.charAt(0).toUpperCase() + w.slice(1))
    .join(" ");
}

// Group the (filtered) routes by tag, preserving the routes.json ordering
// (already sorted by tag, then name) within each section.
const sections = computed(() => {
  const byTag = new Map();
  for (const route of endpoints.value) {
    const tag = route.tag || "other";
    if (!byTag.has(tag)) byTag.set(tag, []);
    byTag.get(tag).push(route);
  }
  return [...byTag.entries()]
    .sort((a, b) => a[0].localeCompare(b[0]))
    .map(([tag, routes]) => ({ tag, title: titleCase(tag), routes }));
});

function authLabel(route) {
  return route.auth ? "JWT" : "Public";
}
</script>

<template>
  <!-- Sections layout: feature-area grouping (like the Bruno collection) -->
  <div v-if="resolvedLayout === 'sections'" class="route-sections">
    <template v-for="section in sections" :key="section.tag">
      <h2 :id="section.tag">{{ section.title }}</h2>
      <div v-for="route in section.routes" :key="route.id" class="route-block">
        <h3 class="route-heading">{{ route.name }}</h3>
        <table class="route-kv">
          <tbody>
            <tr>
              <th>Method</th>
              <td>
                <span
                  class="method"
                  :class="'method-' + (route.method_type || '').toLowerCase()"
                  >{{ route.method_type }}</span
                >
              </td>
            </tr>
            <tr>
              <th>Endpoint URL</th>
              <td><code>{{ route.path }}</code></td>
            </tr>
            <tr>
              <th>Auth</th>
              <td>{{ authLabel(route) }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <p v-if="section.routes.length === 0" class="no-data">No endpoints found.</p>
    </template>
    <p v-if="endpoints.length === 0" class="no-data">No endpoints found.</p>
  </div>

  <!-- Detailed / stacked card: endpoint URL on its own full-width line -->
  <div v-else-if="resolvedLayout === 'detailed'" class="route-cards">
    <div v-for="route in endpoints" :key="route.id" class="route-card">
      <div class="route-card-head">
        <span
          class="method"
          :class="'method-' + (route.method_type || '').toLowerCase()"
          >{{ route.method_type }}</span
        >
        <span class="route-name">{{ route.name }}</span>
        <span class="auth-badge" :class="route.auth ? 'auth-jwt' : 'auth-public'">{{
          authLabel(route)
        }}</span>
      </div>
      <div class="route-url-label">Endpoint URL</div>
      <code class="route-url">{{ route.path }}</code>
      <p v-if="route.description" class="route-desc">{{ route.description }}</p>
    </div>
    <p v-if="endpoints.length === 0" class="no-data">No endpoints found.</p>
  </div>

  <!-- Compact table layout -->
  <div v-else class="table">
    <div class="table-header">
      <div class="header-item" v-for="column in columnsToShow" :key="column">
        {{ columnLabels[column] || column }}
      </div>
    </div>
    <div v-for="route in endpoints" :key="route.id" class="table-row">
      <div class="row-item" v-for="column in columnsToShow" :key="column">
        <span
          v-if="column === 'method_type'"
          class="method"
          :class="'method-' + (route.method_type || '').toLowerCase()"
          >{{ route.method_type }}</span
        >
        <code v-else-if="column === 'path'" class="path-cell">{{ route.path }}</code>
        <span v-else-if="column === 'auth'">{{ authLabel(route) }}</span>
        <span v-else>{{ route[column] }}</span>
      </div>
    </div>
    <p v-if="endpoints.length === 0" class="no-data">No endpoints found.</p>
  </div>
</template>

<style scoped>
/* --- Method pill (shared) --- */
.method {
  font-weight: 700;
  font-size: 0.8em;
  letter-spacing: 0.02em;
}
.method-get {
  color: #3b82f6;
}
.method-post {
  color: #22c55e;
}
.method-put {
  color: #f59e0b;
}
.method-patch {
  color: #a855f7;
}
.method-delete {
  color: #ef4444;
}

/* --- Sections layout (feature-area grouping) --- */
.route-block {
  margin: 0 0 20px;
}
.route-heading {
  margin: 18px 0 8px;
}
table.route-kv {
  display: table;
  width: 100%;
  max-width: 760px;
  margin: 0;
  border-collapse: collapse;
}
table.route-kv th,
table.route-kv td {
  border: 1px solid var(--vp-c-divider);
  padding: 8px 12px;
  text-align: left;
  vertical-align: top;
}
table.route-kv th {
  width: 140px;
  white-space: nowrap;
  background-color: var(--vp-c-bg-soft);
  font-weight: 600;
}
table.route-kv td code {
  font-size: 0.85em;
  overflow-wrap: anywhere;
}

/* --- Detailed / stacked cards --- */
.route-cards {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin: 16px 0;
}
.route-card {
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  padding: 12px 16px;
  background-color: var(--vp-c-bg-soft);
}
.route-card-head {
  display: flex;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
}
.route-name {
  font-weight: 600;
}
.auth-badge {
  font-size: 0.72em;
  font-weight: 600;
  padding: 2px 8px;
  border-radius: 10px;
  border: 1px solid var(--vp-c-divider);
}
.auth-jwt {
  color: var(--vp-c-text-2);
}
.auth-public {
  color: #22c55e;
}
.route-url-label {
  margin-top: 10px;
  font-size: 0.72em;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: var(--vp-c-text-2);
}
.route-url {
  display: block;
  margin-top: 4px;
  padding: 8px 10px;
  width: 100%;
  box-sizing: border-box;
  border-radius: 6px;
  font-size: 0.9em;
  overflow-wrap: anywhere;
  background-color: var(--vp-c-bg);
}
.route-desc {
  margin: 10px 0 0;
  color: var(--vp-c-text-2);
  font-size: 0.92em;
}

/* --- Compact table --- */
.table {
  display: flex;
  flex-direction: column;
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  overflow: hidden;
  margin: 16px 0;
}
.table-header,
.table-row {
  display: flex;
}
.header-item,
.row-item {
  flex: 1;
  padding: 8px 16px;
  text-align: left;
  border-bottom: 1px solid var(--vp-c-divider);
  overflow-wrap: anywhere;
  min-width: 0;
}
.table-header .header-item:nth-child(3),
.table-row .row-item:nth-child(3) {
  flex: 2.5;
}
.table-header {
  background-color: var(--vp-c-bg-soft);
  font-weight: bold;
}
.path-cell {
  font-size: 0.82em;
  overflow-wrap: anywhere;
}
.no-data {
  padding: 16px;
  text-align: center;
}
</style>

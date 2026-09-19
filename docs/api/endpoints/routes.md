<script setup>
import DisplayRoutes from '/docs/components/DisplayRoutes.vue'
</script>

# Routes

Here's a list of the routes you can use to interact with the Aplos NCA SaaS solution.

If you are on a `professional`, `academic`, or `developer` plan you access the API from:

- `https://api.aplos-nca.com`

Team or Enterprise accounts have a dedicated tenancy with an API path unique to their AWS account:

- `https://api.<tenant-name>.aplos-nca.com`
- `https://api.<sandbox>.<tenant-name>.aplos-nca.com` (additional cost)

All routes require a JWT `Authorization: Bearer <token>` header unless marked `Public`.

The routes below are grouped by feature area, mirroring how they are organized
in our Postman and Bruno collections.

> [!TIP]
> This list is generated automatically from our OpenAPI specification, so it always
> reflects the current API. For request/response schemas and an interactive
> "try it out" experience, see the [OpenAPI reference](https://openapi.aplos-nca.com).

<DisplayRoutes layout="sections" />

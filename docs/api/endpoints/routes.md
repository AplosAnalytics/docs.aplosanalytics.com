
<script setup>
import DisplayRoutes from '/docs/components/DisplayRoutes.vue'
</script>

# Routes

Here's a list of our publically available routes that you can use to interact with the Aplos NCA SaaS solution.

If you are on `professional`, `educational` or `developer` plans you will access the API(s) from :

- `https://api.aplos-nca.com`

Team or Enterprise accounts will have a dedicated tenancy and will have an API path unique to their AWS Account

- `https://api.<tenant-name>.aplos-nca.com`
- `https://api.<sandbox>.<tenant-name>.aplos-nca.com` (additional cost)



<DisplayRoutes :columns-to-show="['name', 'path']" />


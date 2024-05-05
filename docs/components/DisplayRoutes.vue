<script setup>
import { ref, computed } from 'vue';
import data from "/docs/api/endpoints/routes.json";
import { defineProps } from 'vue';


const props = defineProps({
  routeNames: {
    type: Array,
    default: () => []
  },
  columnsToShow: {
    type: Array,
    default: () => ['name', 'path', 'description']  // Default columns
  }
});

const columnLabels = {
  name: 'Route Name',
  path: 'Endpoint URL',
  description: 'Description'
};

const endpoints = computed(() => {
  if (props.routeNames.length > 0) {
    return data.routes.filter(route => props.routeNames.includes(route.name));
  }
  return data.routes; // Return all routes if no specific names are provided
});
</script>


<template>
  <div class="table">
    <div class="table-header">
      <div class="header-item" v-for="column in columnsToShow" :key="column">
        {{ columnLabels[column] || column }}
      </div>
    </div>
    <div v-for="route in endpoints" :key="route.name" class="table-row">
      <div class="row-item" v-for="column in columnsToShow" :key="column">
        {{ route[column] }}
      </div>
    </div>
    <p v-if="endpoints.length === 0" class="no-data">No endpoints found.</p>
  </div>
</template>

<style>


.table {
  display: flex;
  flex-direction: column;
  background-color: var(--background-color);
  color: var(--text-color);
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  overflow: hidden;
}

.table-header, .table-row {
  display: flex;
}

.header-item, .row-item {
  flex: 1;
  padding: 8px 16px;
  text-align: left;
  border-bottom: 1px solid var(--vp-c-divider);
}

.table-header {
  background-color: var(--header-bg-color);
  font-weight: bold;
}

.no-data {
  padding: 16px;
  text-align: center;
}

</style>
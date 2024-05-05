<script setup>
import { ref, computed } from "vue";
import data from "/docs/api/endpoints/routes.json";
import { defineProps } from "vue";

const props = defineProps({
  routeId: {
    type: Array,
    default: () => [],
  },
  columnsToShow: {
    type: Array,
    default: () => ["name", "path", "description"], // Default columns
  },
});

const columnLabels = {
  name: "Route Name",
  path: "Endpoint URL",
  description: "Description",
  method_type: "Method Type",
};

const endpoints = computed(() => {
  if (props.routeId.length > 0) {
    return data.routes.filter((route) => props.routeId.includes(route.id));
  }
  return data.routes; // Return all routes if no specific names are provided
});
</script>

<template>
  <div class="markdown-alert markdown-alert-warning">
    <p class="markdown-alert-title">
      <svg
        class="octicon octicon-alert mr-2"
        viewBox="0 0 16 16"
        version="1.1"
        width="16"
        height="16"
        aria-hidden="true"
      >
        <path
          d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"
        ></path></svg
      >Route Warning: Subject to change before Go-Live Summer 2024
    </p>
    <p>
      Some of our routes will be changing prior to our final go-live date this summer
      (2024). They won't change during Early Access, but be sure to check the
      documentation.
    </p>
    <p>
      In order to make a smooth tranistion, we'll provide detailed information on which routes change and which remained the
      same.  As a good programming practice, you store the routes in a central library for easier migration.
    </p>
    <p>
      Older routes may be kept active for short period of time to help with any
      transitions.
    </p>
  </div>

  
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

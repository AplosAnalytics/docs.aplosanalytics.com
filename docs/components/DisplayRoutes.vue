<script setup>
import { computed } from "vue";
import data from "/docs/api/endpoints/routes.json";
import { defineProps } from "vue";

const props = defineProps({
  routeId: {
    type: Array,
    default: () => [],
  },
  // Optional: restrict the table to routes in a single tag/group.
  tag: {
    type: String,
    default: "",
  },
  columnsToShow: {
    type: Array,
    default: () => ["name", "method_type", "path"],
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

const endpoints = computed(() => {
  let routes = data.routes;
  if (props.routeId.length > 0) {
    routes = routes.filter((route) => props.routeId.includes(route.id));
  }
  if (props.tag) {
    routes = routes.filter((route) => route.tag === props.tag);
  }
  return routes;
});

function cellValue(route, column) {
  if (column === "auth") {
    return route.auth ? "JWT" : "Public";
  }
  return route[column];
}
</script>

<template>
  <div class="table">
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
        <code v-else-if="column === 'path'">{{ cellValue(route, column) }}</code>
        <span v-else>{{ cellValue(route, column) }}</span>
      </div>
    </div>
    <p v-if="endpoints.length === 0" class="no-data">No endpoints found.</p>
  </div>
</template>

<style scoped>
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
  overflow-wrap: anywhere;
}

.table-header {
  background-color: var(--vp-c-bg-soft);
  font-weight: bold;
}

.row-item code {
  font-size: 0.85em;
}

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

.no-data {
  padding: 16px;
  text-align: center;
}
</style>

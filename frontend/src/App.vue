<!-- frontend/src/App.vue -->
<template>
  <div id="app" :class="isDarkMode ? 'dark' : 'light'">
    <div class="min-h-screen bg-white dark:bg-gray-900 text-black dark:text-white">
      <div>
        <h1 class="text-4xl font-bold pt-4 mb-1">The Messier Catalog</h1>
      </div>
      <div class="tabs p-4">
        <button @click="goToBoxView" class="btn">
          Box View
        </button>
        <button @click="goToTableView" class="btn">
          Table View
        </button>
        <button @click="toggleTheme" class="btn">
          Toggle Theme
        </button>
      </div>
      <FilterSortOptions v-if="!$route.name || $route.name === 'Box' || $route.name === 'Table'"
        @filter="filterMessierObjects" @sort="sortMessierObjects" />
      <component :is="currentComponent" v-if="!$route.name || $route.name === 'Box' || $route.name === 'Table'">
      </component>
      <router-view :messierObjects="filteredMessierObjects"></router-view>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import FilterSortOptions from "./components/FilterSortOptions.vue";
import MessiersTable from "./components/MessiersTable.vue";
import MessiersBox from "./components/MessiersBox.vue";

export default {
  name: "App",
  components: {
    FilterSortOptions,
    MessiersTable,
    MessiersBox,
  },
  data() {
    return {
      isDarkMode: true,
      currentTab: "box",
      messierObjects: [],
      filteredMessierObjects: [],
      currentMessier: null,
      filterCaptured: null,
      sortOrder: "number",
      reverseSort: false
    };
  },
  computed: {
    currentComponent() {
      return this.currentTab === "box" ? MessiersBox : MessiersTable;
    },
  },
  mounted() {
    this.fetchMessierObjects();
    this.isDarkMode = localStorage.getItem("isDarkMode") === "false" ? true : false; // Dark mode by default
    localStorage.setItem("isDarkMode", this.isDarkMode);
  },
  methods: {
    fetchMessierObjects() {
      const params = {
        sort_by: this.sortOrder,
        reverse_sort: this.reverseSort,
        filter_captured: this.filterCaptured,
        filter_season: this.filterSeason,
        filter_type: this.filterType,
        filter_constellation: this.filterConstellation,
      };

      axios
        .get("http://localhost:5000/api/messier", { params })
        .then((response) => {
          this.messierObjects = response.data;
          this.filteredMessierObjects = response.data;
        })
        .catch((error) => {
          console.error("Error fetching Messier objects:", error);
        });
    },
    filterMessierObjects({ captured, season, type, constellation }) {
      this.filterCaptured = captured;
      this.filterSeason = season;
      this.filterType = type;
      this.filterConstellation = constellation;
      this.fetchMessierObjects();
    },
    sortMessierObjects({ sortOrder, reverseSort }) {
      this.sortOrder = sortOrder;
      this.reverseSort = reverseSort;
      this.fetchMessierObjects();
    },
    goToBoxView() {
      this.currentTab = "box";
      this.$router.push({ name: "Box" });
    },
    goToTableView() {
      this.currentTab = "table";
      this.$router.push({ name: "Table" });
    },
    toggleTheme() {
      this.isDarkMode = !this.isDarkMode;
    },
    onRouteChange() {
      // console.log('Route changed');
    },
  },
};
</script>

<style>
#app {
  text-align: center;
}

.btn {
  @apply py-2 px-4 m-2 cursor-pointer transition-colors duration-300;
}

.dark .btn {
  @apply bg-gray-700 text-white hover:bg-gray-600;
}

.btn {
  @apply bg-gray-200 text-gray-900 hover:bg-gray-300;
}

.image-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.image-item {
  width: 20%;
  /* Each item takes up 10% of the container width, fitting 10 in a row */
}

.image-item img {
  width: 100%;
  /* Make image fill the container */
  height: auto;
  /* Keep the aspect ratio */
}

.caption {
  text-align: center;
}

.tabs button {
  padding: 10px;
  margin: 5px;
  cursor: pointer;
}

@media (min-width: 768px) {
  .image-item {
    width: 12%;
    /* Fit 10 images per row on medium and larger screens */
  }
}
</style>

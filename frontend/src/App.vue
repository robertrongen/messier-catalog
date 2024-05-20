<!-- frontend/src/App.vue -->
<template>
  <div id="app" class="dark:bg-gray-900 dark:text-white">
    <div class="tabs">
      <button @click="goToBoxView" class="bg-gray-800 text-white">Box View</button>
      <button @click="goToTableView" class="bg-gray-800 text-white">Table View</button>
    </div>
    <FilterSortOptions 
      v-if="!$route.name || $route.name === 'Box' || $route.name === 'Table'"
      @filter="filterMessierObjects" 
      @sort="sortMessierObjects" 
    />
    <component 
      :is="currentComponent" 
      v-if="!$route.name || $route.name === 'Box' || $route.name === 'Table'"
    ></component>
    <router-view :messierObjects="filteredMessierObjects"></router-view> <!-- Pass messierObjects as props -->
  </div>
</template>

<script>
import axios from 'axios';
import FilterSortOptions from './components/FilterSortOptions.vue';
import MessiersTable from './components/MessiersTable.vue';
import MessiersBox from './components/MessiersBox.vue';

export default {
  name: 'App',
  components: {
    FilterSortOptions,
    MessiersTable,
    MessiersBox
  },
  data() {
    return {
      isDarkMode: true,
      currentTab: 'box',
      messierObjects: [],
      filteredMessierObjects: [],
      currentMessier: null,
      filterCaptured: null,
      sortOrder: 'number'
    };
  },
  computed: {
    currentComponent() {
      return this.currentTab === 'box' ? MessiersBox : MessiersTable;
    },
    appClasses() {
      return {
        'dark': this.isDarkMode
      };
    }

  },
  mounted() {
    this.fetchMessierObjects();
  },
  methods: {
    fetchMessierObjects() {
      const params = {
        sort_by: this.sortOrder,
        filter_captured: this.filterCaptured,
        filter_season: this.filterSeason,
        filter_type: this.filterType,
        filter_constellation: this.filterConstellation,
      };

      axios.get('http://localhost:5000/api/messier', { params })
      .then(response => {
        this.messierObjects = response.data;
        this.filteredMessierObjects = response.data;
      })
      .catch(error => {
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
    sortMessierObjects(order) {
      this.sortOrder = order;
      this.fetchMessierObjects();
    },
    goToBoxView() {
      this.currentTab = 'box';
      this.$router.push({ name: 'Box' });
    },
    goToTableView() {
      this.currentTab = 'table';
      this.$router.push({ name: 'Table' });
    },
    onRouteChange() {
      // console.log('Route changed');
    }
  }
}
</script>

<style>
  #app {
    text-align: center;
  }
  .image-grid {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
  }
  .image-item {
    width: 20%; /* Each item takes up 10% of the container width, fitting 10 in a row */
  }
  .image-item img {
    width: 100%; /* Make image fill the container */
    height: auto; /* Keep the aspect ratio */
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
      width: 12%; /* Fit 10 images per row on medium and larger screens */
    }
  }
</style>

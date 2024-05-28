<!-- frontend/src/App.vue -->
<template>
  <div id="app" :class="isDarkMode ? 'dark' : 'light'">
    <div class="min-h-screen bg-white dark:bg-gray-900 text-black dark:text-white">
      <div>
        <h1 class="text-4xl font-bold pt-4 mb-1">The Messier Catalog</h1>
        <div v-if="isAuthenticated" class="text-right pr-4">
          <span>Logged in as {{ username }}</span>
          <span v-if="isAdmin"> (with admin role)</span>
        </div>
      </div>
      <div class="tabs p-4">
        <button @click="goToBoxView" class="btn">Box View</button>
        <button @click="goToTableView" class="btn">Table View</button>
        <button @click="toggleTheme" class="btn">Toggle Theme</button>
        <button v-if="!isAuthenticated" @click="goToLogin" class="btn">Login</button>
        <button v-if="isAuthenticated" @click="logout" class="btn">Logout</button>
        <button v-if="isAuthenticated" @click="goToProfile" class="btn">Profile</button>
        <button v-if="isAdmin" @click="goToAdmin" class="btn">Admin</button>
      </div>
      <FilterSortOptions v-if="!$route.name || $route.name === 'Box' || $route.name === 'Table'"
        @filter="filterMessierObjects" @sort="sortMessierObjects" />
      <component :is="currentComponent" v-if="!$route.name || $route.name === 'Box' || $route.name === 'Table'">
      </component>
      <router-view :messierObjects="filteredMessierObjects" @update-auth-status="checkAuth"></router-view>
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
      currentMessier: null,
      messierObjects: [],
      filteredMessierObjects: [],
      filterSeason: null,
      filterType: null,
      filterConstellation: null,
      filterCaptured: null,
      filterPlanned: null,
      sortOrder: "number",
      reverseSort: false,
      isAuthenticated: false,
      isAdmin: false,
      username: '',
      user: null
    };
  },
  computed: {
    currentComponent() {
      return this.currentTab === "box" ? MessiersBox : MessiersTable;
    },
  },
  mounted() {
    this.fetchMessierObjects();
    this.checkAuth();
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
        filter_planned: this.filterPlanned
      };

      axios
        .get(`${process.env.VUE_APP_API_BASE_URL}/messier`, { params })
        .then((response) => {
          this.messierObjects = response.data;
          this.filteredMessierObjects = response.data;
        })
        .catch((error) => {
          console.error("Error fetching Messier objects:", error);
        });
    },
    filterMessierObjects({ captured, season, type, constellation, planned }) {
      this.filterCaptured = captured;
      this.filterSeason = season;
      this.filterType = type;
      this.filterConstellation = constellation;
      this.filterPlanned = planned;
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
    checkAuth() {
      const token = localStorage.getItem("token");
      if (token) {
        axios.get(`${process.env.VUE_APP_API_BASE_URL}/profile`, {
          headers: {
            Authorization: `Bearer ${token}`
          }
        })
          .then(response => {
            this.isAuthenticated = true;
            this.user = response.data;
            this.username = response.data.username;
            this.isAdmin = response.data.roles.includes('admin');
          })
          .catch(error => {
            console.error("Error fetching user profile:", error);
            this.isAuthenticated = false;
          });
      } else {
        this.isAuthenticated = false;
      }
    },
    goToLogin() {
      this.$router.push({ name: "LoginComponent" });
    },
    logout() {
      localStorage.removeItem("token");
      this.isAuthenticated = false;
      this.isAdmin = false;
      this.user = null;
      this.$router.push({ name: "Box" });
    },
    goToProfile() {
      this.$router.push({ name: "UserProfile" });
    },
    goToAdmin() {
      this.$router.push({ name: "AdminComponent" });
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

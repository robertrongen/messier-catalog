<template>
  <div id="app">
    <div class="tabs">
      <button @click="currentTab = 'table'">Table View</button>
      <button @click="currentTab = 'box'">Box View</button>
    </div>
    <component :is="currentComponent" :messierObjects="messierObjects"/>
  </div>
</template>

<script>
import axios from 'axios';
import MessiersTable from './components/MessiersTable';
import MessiersBox from './components/MessiersBox';

export default {
  name: 'App',
  components: {
    MessiersTable,
    MessiersBox
  },
  data() {
    return {
      currentTab: 'table',
      messierObjects: []
    };
  },
  computed: {
    currentComponent() {
      return this.currentTab === 'table' ? MessiersTable : MessiersBox;
    }
  },
  mounted() {
    this.fetchMessierObjects();
  },
  methods: {
    fetchMessierObjects() {
      axios.get('http://localhost:5000/api/messier')
        .then(response => {
          this.messierObjects = response.data;
        })
        .catch(error => {
          console.error("Error fetching Messier objects:", error);
        });
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
    padding: 5px; /* Adjust padding to manage spacing */
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
      width: 10%; /* Fit 10 images per row on medium and larger screens */
    }
  }
</style>

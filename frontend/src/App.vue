<!-- frontend/src/App.vue -->
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
import MessiersTable from './components/MessiersTable'
import MessiersBox from './components/MessiersBox'
import axios from 'axios'

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
    }
  },
  computed: {
    currentComponent() {
      return this.currentTab === 'table' ? MessiersTable : MessiersBox;
    }
  },
  mounted() {
    axios.get('/api/messier')
      .then(response => {
        this.messierObjects = response.data;
      })
      .catch(error => {
        console.error("Error fetching Messier objects:", error);
      });
  }
}
</script>

<style>
#app {
  text-align: center;
}
.tabs button {
  padding: 10px;
  margin: 5px;
  cursor: pointer;
}
</style>

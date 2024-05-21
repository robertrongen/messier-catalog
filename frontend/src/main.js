// src/main.js
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import './assets/tailwind.css'; // Import Tailwind CSS
import axios from 'axios';

console.log('API Base URL:', process.env.VUE_APP_API_BASE_URL);
axios.defaults.baseURL = process.env.VUE_APP_API_BASE_URL;

createApp(App).use(router).mount('#app');
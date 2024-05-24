import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import './assets/tailwind.css';
import axios from 'axios';

axios.defaults.baseURL = process.env.VUE_APP_API_BASE_URL;

const app = createApp(App);
app.use(router);
app.config.globalProperties.$http = axios;
app.mount('#app');

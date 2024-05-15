// frontend/src/router/index.js
import Vue from 'vue';
import Router from 'vue-router';
import MessiersTable from '../components/MessiersTable';

Vue.use(Router);

export default new Router({
    routes: [
        {
            path: '/',
            name: 'Messiers',
            component: MessiersTable
        },
        // Additional routes can be added here
    ]
});

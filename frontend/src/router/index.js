// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import MessiersTable from '../components/MessiersTable.vue';
import MessiersBox from '../components/MessiersBox.vue';
import MessierDetail from '../components/MessierDetail.vue';

const routes = [
    {
        path: '/',
        name: 'Box',
        component: MessiersBox,
        props: route => ({ messierObjects: route.query.messierObjects }) // Pass messierObjects as props
    },
    {
        path: '/table',
        name: 'Table',
        component: MessiersTable,
        props: route => ({ messierObjects: route.query.messierObjects }) // Pass messierObjects as props
    },
    {
        path: '/messier/:id',
        name: 'MessierDetail',
        component: MessierDetail,
        props: route => ({ id: route.params.id, messierObjects: route.query.messierObjects }) // Pass messierObjects as props
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;

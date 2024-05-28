// src/router/index.js
import { createRouter, createWebHistory } from "vue-router";
import MessiersTable from "../components/MessiersTable.vue";
import MessiersBox from "../components/MessiersBox.vue";
import MessierDetail from "../components/MessierDetail.vue";
import PrivacyPolicy from "@/components/PrivacyPolicy.vue";
import TermsOfService from "@/components/TermsOfService.vue";
import LoginComponent from "@/components/LoginComponent.vue";
import OAuthCallback from "@/components/OAuthCallback.vue";
import UserProfile from "@/components/UserProfile.vue";
import AdminComponent from "@/components/AdminComponent.vue";

const routes = [
    {
        path: "/",
        name: "Box",
        component: MessiersBox,
        props: (route) => ({ messierObjects: route.query.messierObjects }), // Pass messierObjects as props
    },
    {
        path: "/table",
        name: "Table",
        component: MessiersTable,
        props: (route) => ({ messierObjects: route.query.messierObjects }), // Pass messierObjects as props
    },
    {
        path: "/messier/:id",
        name: "MessierDetail",
        component: MessierDetail,
        props: (route) => ({
            id: route.params.id,
            messierObjects: route.query.messierObjects,
        }), // Pass messierObjects as props
    },
    {
        path: "/privacy-policy",
        name: "PrivacyPolicy",
        component: PrivacyPolicy,
    },
    {
        path: "/terms-of-service",
        name: "TermsOfService",
        component: TermsOfService,
    },
    {
        path: "/login",
        name: "LoginComponent",
        component: LoginComponent,
    },
    {
        path: "/auth/callback",
        name: "OAuthCallback",
        component: OAuthCallback,
    },
    {
        path: "/profile",
        name: "UserProfile",
        component: UserProfile,
    },
    {
        path: "/admin",
        name: "Admin",
        component: AdminComponent,
    }
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

export default router;

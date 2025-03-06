<!-- frontend/src/components/LoginComponent.vue -->
<template>
    <div class="flex items-center justify-center min-h-screen bg-gray-100">
        <div class="w-full max-w-md p-8 space-y-6 bg-white shadow-md rounded-lg">
            <h2 class="text-2xl font-bold text-center text-gray-800">Login</h2>
            <form @submit.prevent="login" class="space-y-4">
                <div>
                    <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
                    <input v-model="email" id="email" type="email" placeholder="Email"
                        class="w-full px-3 py-2 mt-1 text-gray-700 border border-gray-300 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500" />
                </div>
                <div>
                    <label for="password" class="block text-sm font-medium text-gray-700">Password</label>
                    <input v-model="password" id="password" type="password" placeholder="Password"
                        class="w-full px-3 py-2 mt-1 text-gray-700 border border-gray-300 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500" />
                </div>
                <div class="flex items-center justify-between">
                    <button type="submit"
                        class="px-4 py-2 text-white bg-indigo-600 rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500">
                        Login
                    </button>
                    <button type="button" @click="resetPassword"
                        class="text-sm text-indigo-600 hover:underline focus:outline-none">
                        Forgot Password?
                    </button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            email: '',
            password: ''
        }
    },
    methods: {
        login() {
            axios.post(`${process.env.VUE_APP_API_BASE_URL}/auth/login`, { email: this.email, password: this.password })
                .then(response => {
                    localStorage.setItem('token', response.data.token);
                    localStorage.setItem('username', response.data.username);
                    localStorage.setItem('role', response.data.role);
                    this.$emit('update-auth-status', true);
                    this.$router.push({ name: 'Box' });
                    pendo.initialize({
                        visitor: {
                        id: response.data.username,
                        email: this.email,
                        }
                    });
                })
                .catch(error => {
                    console.error(error);
                });
        },
        resetPassword() {
            axios.post(`${process.env.VUE_APP_API_BASE_URL}/auth/reset_password`, { email: this.email })
                .then(() => {
                    alert('Password reset email sent');
                })
                .catch(error => {
                    console.error(error);
                });
        }
    }
}
</script>

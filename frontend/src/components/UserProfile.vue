<!-- /frontend/src/components/UserProfile.vue -->
<template>
    <div class="flex items-center justify-center min-h-screen bg-gray-100">
        <div class="w-full max-w-md p-8 space-y-6 bg-white shadow-md rounded-lg">
            <div class="p-4">
                <h2 class="text-2xl font-bold mb-4">User Profile</h2>
                <form @submit.prevent="updateProfile">
                    <input v-model="username" placeholder="Username" class="form-input mt-1 block w-full mb-4">
                    <button type="submit" class="px-4 py-2 bg-blue-500 text-white rounded">Update Profile</button>
                </form>
                <h2 class="text-2xl font-bold mt-8 mb-4">Annotations</h2>
                <AnnotationComponent />
            </div>
            <h2 class="text-2xl font-bold text-center text-gray-800">User Profile</h2>
            <form @submit.prevent="updateProfile" class="space-y-4">
                <div>
                    <label for="username" class="block text-sm font-medium text-gray-700">Username</label>
                    <input v-model="username" id="username" type="text" placeholder="Username"
                        class="w-full px-3 py-2 mt-1 text-gray-700 border border-gray-300 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500" />
                </div>
                <div class="flex items-center justify-between">
                    <button type="submit"
                        class="px-4 py-2 text-white bg-indigo-600 rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500">
                        Update Profile
                    </button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import AnnotationComponent from './AnnotationComponent.vue';

export default {
    components: {
        AnnotationComponent
    },
    data() {
        return {
            username: ''
        }
    },
    created() {
        this.fetchProfile();
    },
    methods: {
        fetchUserProfile() {
            axios.get(`${process.env.VUE_APP_API_BASE_URL}/profile`, {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('token')}`
                }
            })
                .then(response => {
                    this.username = response.data.username;
                })
                .catch(error => {
                    console.error(error);
                });
        },
        updateProfile() {
            axios.post(`${process.env.VUE_APP_API_BASE_URL}/profile`, { username: this.username }, {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('token')}`
                }
            })
                .then(() => {
                    alert('Profile updated');
                })
                .catch(error => {
                    console.error(error);
                });
        }
    }
}
</script>

<style scoped>
.form-input {
    @apply border-gray-300 rounded-md shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50;
}
</style>

<!-- /frontend/src/components/AdminComponent.vue -->
<template>
    <div class="flex items-center justify-center min-h-screen bg-gray-100">
        <div class="w-full max-w-4xl p-8 space-y-6 bg-white shadow-md rounded-lg">
            <h2 class="text-2xl font-bold text-center text-gray-800">Admin - Manage Users</h2>
            <table class="table-auto w-full text-left border-collapse border border-gray-200 dark:border-gray-700 mb-4">
                <thead>
                    <tr class="border-t border-gray-200 dark:border-gray-700">
                        <th class="py-2 px-4">Email</th>
                        <th class="py-2 px-4">Role</th>
                        <th class="py-2 px-4">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="user in users" :key="user.id" class="border-t border-gray-200 dark:border-gray-700">
                        <td class="py-2 px-4">{{ user.email }}</td>
                        <td class="py-2 px-4">
                            <select v-model="user.role" @change="updateRole(user)" class="form-select mt-1 block w-full">
                                <option v-for="role in roles" :key="role.id" :value="role.name">{{ role.name }}</option>
                            </select>
                        </td>
                        <td class="py-2 px-4">
                            <button @click="removeUser(user.id)" class="px-4 py-2 text-white bg-red-600 rounded-md hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-500">Remove</button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            users: [],
            roles: []
        }
    },
    created() {
        axios.get('/api/admin/users', {
            headers: {
                Authorization: `Bearer ${localStorage.getItem('token')}`
            }
        })
            .then(response => {
                this.users = response.data.users;
                this.roles = response.data.roles;
            })
            .catch(error => {
                console.error(error);
            });
    },
    methods: {
        updateRole(user) {
            axios.post(`${process.env.VUE_APP_API_BASE_URL}/admin/role/${user.id}`, { role: user.role }, {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('token')}`
                }
            })
            .then(() => {
                alert('Role updated');
            })
            .catch(error => {
                console.error(error);
            });
        },
        removeUser(userId) {
            axios.delete(`${process.env.VUE_APP_API_BASE_URL}/admin/user/${userId}`, {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('token')}`
                }
            })
            .then(() => {
                this.users = this.users.filter(user => user.id !== userId);
            })
            .catch(error => {
                console.error(error);
            });
        },
        fetchAdminData() {
                axios.get(`${process.env.VUE_APP_API_BASE_URL}/admin/users`, {
                    headers: {
                        Authorization: `Bearer ${localStorage.getItem('token')}`
                    }
                })
                .then(response => {
                    this.users = response.data.users;
                    this.roles = response.data.roles;
                })
                .catch(error => {
                    console.error(error);
                });
            },
        }
    }
</script>

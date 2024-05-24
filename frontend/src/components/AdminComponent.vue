<template>
    <div>
        <h2>Admin - Manage Users</h2>
        <table>
            <thead>
                <tr>
                    <th>Email</th>
                    <th>Role</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="user in users" :key="user.id">
                    <td>{{ user.email }}</td>
                    <td>
                        <select v-model="user.role" @change="updateRole(user)">
                            <option v-for="role in roles" :value="role.name">{{ role.name }}</option>
                        </select>
                    </td>
                    <td><button @click="removeUser(user.id)">Remove</button></td>
                </tr>
            </tbody>
        </table>
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
            axios.post(`/api/admin/role/${user.id}`, { role: user.role }, {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('token')}`
                }
            })
                .then(response => {
                    alert('Role updated');
                })
                .catch(error => {
                    console.error(error);
                });
        },
        removeUser(userId) {
            axios.delete(`/api/admin/user/${userId}`, {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('token')}`
                }
            })
                .then(response => {
                    this.users = this.users.filter(user => user.id !== userId);
                })
                .catch(error => {
                    console.error(error);
                });
        }
    }
}
</script>
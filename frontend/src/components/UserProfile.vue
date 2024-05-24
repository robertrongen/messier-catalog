<template>
    <div>
        <h2>User Profile</h2>
        <form @submit.prevent="updateProfile">
            <input v-model="username" placeholder="Username">
            <button type="submit">Update Profile</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            username: ''
        }
    },
    created() {
        axios.get('/api/profile', {
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
    methods: {
        updateProfile() {
            axios.post('/api/profile', { username: this.username }, {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('token')}`
                }
            })
                .then(response => {
                    alert('Profile updated');
                })
                .catch(error => {
                    console.error(error);
                });
        }
    }
}
</script>
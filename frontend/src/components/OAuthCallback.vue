<template>
    <div>Loading...</div>
</template>

<script>
export default {
    mounted() {
        const fragment = new URLSearchParams(window.location.hash.slice(1));
        const accessToken = fragment.get('access_token');

        if (accessToken) {
            // Save the token to local storage or Vuex store
            localStorage.setItem('access_token', accessToken);
            // Redirect to the home page or another route
            this.$router.push({ name: 'Home' });
        } else {
            // Handle the error
            console.error('Authentication failed');
        }
    }
};
</script>
<!-- frontend/src/components/FilterSort.vue -->
<template>
    <div class="filter-sort">
        <div class="filter">
            <input type="text" v-model="filterQuery" placeholder="Filter by name..." @input="onFilter" />
        </div>
        <div class="sort">
            <select v-model="sortOrder" @change="onSort">
            <option value="number">Sort by Number</option>
            <option value="season">Sort by Season</option>
            <option value="type">Sort by Type</option>
            <option value="magnitude">Sort by Magnitude</option>
            </select>
        </div>
        </div>
    </template>
    
    <script>
    export default {
        name: 'FilterSortOptions',
        data() {
            return {
                filterQuery: '',
                sortOrder: 'number' // Default sort order
            };
        },
        methods: {
            onFilter() {
                this.$emit('filter', this.filterQuery);
            },
            onSort() {
                this.$emit('sort', this.sortOrder);
            }
        }
    }
</script>
    
<style>
    .filter-sort {
        display: flex;
        justify-content: space-between;
        margin: 10px 0;
    }
    .filter input {
        padding: 8px;
    }
    .sort select {
        padding: 8px;
    }
</style>

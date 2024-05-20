<!-- frontend/src/components/FilterSortOptions.vue -->
<template>
    <div class="flex justify-between p-4">
        <div class="flex space-x-4">
            <select v-model="filterSeason" @change="onFilter"
                class="filter-select form-select block w-full mt-1 dark:bg-gray-700 dark:text-white">
                <option value="">All Seasons</option>
                <option value="Winter">Winter</option>
                <option value="Spring">Spring</option>
                <option value="Summer">Summer</option>
                <option value="Autumn">Autumn</option>
            </select>
            <select v-model="filterType" @change="onFilter"
                class="filter-select form-select block w-full mt-1 dark:bg-gray-700 dark:text-white">
                <option value="">All Types</option>
                <option value="Nebula">Nebula</option>
                <option value="Cluster">Cluster</option>
                <option value="Galaxy">Galaxy</option>
            </select>
            <select v-model="filterConstellation" @change="onFilter"
                class="filter-select form-select block w-full mt-1 dark:bg-gray-700 dark:text-white">
                <option value="">All Constellations</option>
                <option value="Andromeda">Andromeda</option>
                <option value="Aquarius">Aquarius</option>
                <option value="Auriga">Auriga</option>
                <option value="Cancer">Cancer</option>
                <option value="Canes Venatici">Canes Venatici</option>
                <option value="Canis Major">Canis Major</option>
                <option value="Capricornus">Capricornus</option>
                <option value="Cassiopeia">Cassiopeia</option>
                <option value="Cetus">Cetus (Wail)</option>
                <option value="Coma Berenices">Coma Berenices</option>
                <option value="Corvus">Corvus (Crow)</option>
                <option value="Cygnus">Cygnus</option>
                <option value="Draco">Draco</option>
                <option value="Gemini">Gemini</option>
                <option value="Hercules">Hercules</option>
                <option value="Hydra">Hydra</option>
                <option value="Leo">Leo</option>
                <option value="Lyra">Lyra</option>
                <option value="Monoceros">Monoceros</option>
                <option value="Ophiuchus">Ophiuchus (Serpent Bearer)</option>
                <option value="Orion">Orion</option>
                <option value="Pegasus">Pegasus</option>
                <option value="Perseus">Perseus</option>
                <option value="Pisces">Pisces</option>
                <option value="Puppis">Puppis</option>
                <option value="Sagittarius">Sagittarius</option>
                <option value="Scorpius">Scorpius</option>
                <option value="Scutum">Scutum (Shield)</option>
                <option value="Serpens">Serpens</option>
                <option value="Taurus">Taurus</option>
                <option value="Triangulum">Triangulum</option>
                <option value="Virgo">Virgo</option>
                <option value="Vulpecula">Vulpecula</option>
            </select>
            <select v-model="filterCaptured" @change="onFilter"
                class="filter-select form-select block w-full mt-1 dark:bg-gray-700 dark:text-white">
                <option value="">All</option>
                <option value="1">Captured</option>
                <option value="0">Not Captured</option>
            </select>
        </div>
        <div class="flex items-center space-x-4">
            <select v-model="sortOrder" @change="onSort"
                class="sort-select form-select block w-full mt-1 dark:bg-gray-700 dark:text-white">
                <option value="number">Sort by Number</option>
                <option value="season">Sort by Season</option>
                <option value="type">Sort by Type</option>
                <option value="magnitude">Sort by Magnitude</option>
                <option value="dec">Sort by Declination</option>
            </select>
        </div>
        <div class="flex items-center">
            <input type="checkbox" id="reverseSort" v-model="reverseSort" @change="onSort"
                class="form-checkbox h-5 w-5 text-gray-600 dark:text-gray-400">
            <label for="reverseSort" class="ml-2 dark:text-white">Reverse Order</label>
        </div>
    </div>
</template>

<script>
export default {
    name: 'FilterSortOptions',
    data() {
        return {
            filterCaptured: '',
            filterSeason: '',
            filterType: '',
            filterConstellation: '',
            sortOrder: 'number',
            reverseSort: false
        };
    },
    methods: {
        onFilter() {
            this.$emit('filter', {
                captured: this.filterCaptured,
                season: this.filterSeason,
                type: this.filterType,
                constellation: this.filterConstellation,
            });
        },
        onSort() {
            this.$emit('sort', {
                sortOrder: this.sortOrder,
                reverseSort: this.reverseSort
            });
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

.filter input,
.filter select {
    padding: 8px;
    margin-right: 5px;
}

.sort select {
    padding: 8px;
}
</style>
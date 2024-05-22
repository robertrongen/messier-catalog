<!-- frontend/src/components/MessiersTable.vue -->
<template>
    <div class="p-4">
        <table class="min-w-full divide-y divide-gray-200 dark:divide-gray-700">
            <thead class="bg-gray-50 dark:bg-gray-700">
                <tr>
                    <th class="p-2 text-left">Messier</th>
                    <th class="p-2 text-left">NGC</th>
                    <th class="p-2 text-left">Name</th>
                    <th class="p-2 text-left">Type</th>
                    <th class="p-2 text-left">Sub Type</th>
                    <th class="p-2 text-left">Season</th>
                    <th class="p-2 text-left">Constellation</th>
                    <th class="p-2 text-left">Magnitude</th>
                    <th class="p-2 text-left">Size</th>
                    <!-- <th class="p-2 text-left">Distance (ly)</th> -->
                    <!-- <th class="p-2 text-left">Right Ascension</th> -->
                    <th class="p-2 text-left">Declination</th>
                    <th class="p-2 text-left">Captured</th>
                    <!-- <th class="p-2 text-left">Capture Year</th> -->
                    <th class="p-2 text-left">Planned?</th>
                    <!-- <th class="p-2 text-left">Remarks</th> -->
                </tr>
            </thead>
            <tbody class="bg-white dark:bg-gray-800 divide-y divide-gray-200 dark:divide-gray-700">
                <tr v-for="object in messierObjects" :key="object.Messier">
                    <td class="text-left p-2">
                        <router-link :to="{ name: 'MessierDetail', params: { id: object.Messier } }">
                            {{ object.Messier }}
                        </router-link>
                    </td>
                    <td class="text-right p-2">{{ object.NGC }}</td>
                    <td class="text-left p-2">{{ object.Name }}</td>
                    <td class="text-left p-2">{{ object.Type }}</td>
                    <td class="text-left p-2">{{ object.SubType }}</td>
                    <td class="text-left p-2">{{ object.Season }}</td>
                    <td class="text-left p-2">{{ object.Constellation }}</td>
                    <td class="text-right p-2">{{ object.Magnitude }}</td>
                    <td class="text-right p-2">{{ object.Size }}</td>
                    <!-- <td class="text-right p-2">{{ object.Distance }}</td> -->
                    <!-- <td class="text-right p-2">{{ object.RA }}</td> -->
                    <td class="text-right p-2">{{ object.Dec }}</td>
                    <td class="text-left p-2">{{ object.Captured ? 'Yes' : 'No' }}</td>
                    <!-- <td class="text-right p-2">{{ object.CapYear }}</td> -->
                    <td class="text-right p-2">{{ object.Planned }}</td>
                    <!-- <td class="text-left p-2">{{ object.Remarks }}</td> -->
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    name: 'MessiersTable',
    props: {
        messierObjects: Array
    }
}
</script>

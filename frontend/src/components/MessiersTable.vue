<!-- frontend/src/components/MessiersTable.vue -->
<template>
    <div class="MessiersTable">
        <table>
            <thead>
                <tr>
                    <th>Messier</th>
                    <th>NGC</th>
                    <th>Name</th>
                    <th>Type</th>
                    <th>Sub Type</th>
                    <th>Season</th>
                    <th>Constellation</th>
                    <th>Magnitude</th>
                    <th>Size</th>
                    <th>Distance (ly)</th>
                    <th>Right Ascension</th>
                    <th>Declination</th>
                    <th>Captured</th>
                    <th>Capture Year</th>
                    <th>Remarks</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="object in messierObjects" :key="object.Messier">
                    <td><router-link :to="{ name: 'MessierDetail', params: { id: object.Messier } }">{{ object.Messier }}</router-link></td>
                    <td>{{ object.NGC }}</td>
                    <td>{{ object.Name }}</td>
                    <td>{{ object.Type }}</td>
                    <td>{{ object.SubType }}</td>
                    <td>{{ object.Season }}</td>
                    <td>{{ object.Constellation }}</td>
                    <td>{{ object.Magnitude }}</td>
                    <td>{{ object.Size }}</td>
                    <td>{{ object.Distance }}</td>
                    <td>{{ object.RightAscension }}</td>
                    <td>{{ object.Declination }}</td>
                    <td>{{ object.Captured ? 'Yes' : 'No' }}</td>
                    <td>{{ object.CapYear }}</td>
                    <td>{{ object.Remarks }}</td>
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

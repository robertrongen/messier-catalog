<template>
    <div class="MessiersTable">
        <table>
            <thead>
                <tr>
                    <th>Messier</th>
                    <th>NGC</th>
                    <th>Name</th>
                    <th>Type</th>
                    <th>Season</th>
                    <th>Magnitude</th>
                    <th>Cons</th>
                    <th>Constellation</th>
                    <th>Latin</th>
                    <th>RA</th>
                    <th>Dec</th>
                    <th>Distance (light-years)</th>
                    <th>Size</th>
                    <th>Discoverer</th>
                    <th>Year of Discovery</th>
                    <th>Captured</th>
                    <th>Capture Year</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="object in messierObjects" :key="object.Messier">
                    <td>{{ object.Messier }}</td>
                    <td>{{ object.NGC }}</td>
                    <td>{{ object.Name }}</td>
                    <td>{{ object.Type }}</td>
                    <td>{{ object.Season }}</td>
                    <td>{{ object.Magnitude }}</td>
                    <td>{{ object.Cons }}</td>
                    <td>{{ object.Constellation }}</td>
                    <td>{{ object.Latin }}</td>
                    <td>{{ object.RA }}</td>
                    <td>{{ object.Dec }}</td>
                    <td>{{ object.Distance }}</td>
                    <td>{{ object.Size }}</td>
                    <td>{{ object.Discoverer }}</td>
                    <td>{{ object.Year }}</td>
                    <td>{{ object.Captured ? 'Yes' : 'No' }}</td>
                    <td>{{ object.CapYear }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    name: 'MessiersTable',
    props: {
        msg: String
    }
}
</script>

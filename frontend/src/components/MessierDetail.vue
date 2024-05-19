<!-- frontend/src/components/MessierDetail.vue -->
<template>
    <div>
        <h2>Messier Object {{ messier.Messier }}</h2>
        <table>
            <tr><td>NGC</td><td>{{ messier.NGC }}</td></tr>
            <tr><td>Name</td><td>{{ messier.Name }}</td></tr>
            <tr><td>Type</td><td>{{ messier.Type }}</td></tr>
            <tr><td>Season</td><td>{{ messier.Season }}</td></tr>
            <tr><td>Magnitude</td><td>{{ messier.Magnitude }}</td></tr>
            <tr><td>Constellation</td><td>{{ messier.Constellation }}</td></tr>
            <tr><td>RA</td><td>{{ messier.RA }}</td></tr>
            <tr><td>Dec</td><td>{{ messier.Dec }}</td></tr>
            <tr><td>Distance</td><td>{{ messier.Distance }}</td></tr>
            <tr><td>Size</td><td>{{ messier.Size }}</td></tr>
            <tr><td>Discoverer</td><td>{{ messier.Discoverer }}</td></tr>
            <tr><td>Year</td><td>{{ messier.Year }}</td></tr>
            <tr><td>Captured</td><td>{{ messier.Captured }}</td></tr>
            <tr><td>Capture Year</td><td>{{ messier.CapYear }}</td></tr>
            <tr><td>Remarks</td><td>{{ messier.Remarks }}</td></tr>
        </table>
        <div class="navigation-buttons">
            <button @click="goToPreviousMessier" :disabled="!hasPrevious">Previous</button>
            <button @click="goToNextMessier" :disabled="!hasNext">Next</button>
        </div>
        <div class="annotations">
            <h3>Add/Edit Annotation</h3>
            <input type="number" v-model="newCaptured" placeholder="Captured (0 or 1)">
            <input type="number" v-model="newCapYear" placeholder="Capture Year">
            <textarea v-model="newRemark" placeholder="Add annotation content..."></textarea>
            <button @click="updateAnnotation">Save Annotation</button>
        </div>
        <div class="images">
            <img :src="atlasImagePath" alt="atlas Image" v-if="atlasImagePath">
            <img :src="roroImagePath" alt="roro Image" v-if="roroImagePath">
        </div>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: 'MessierDetail',
        props: {
            id: String,
            messierObjects: Array
        },
        data() {
            return {
                messier: {},
                atlasImagePath: null,
                roroImagePath: null,
                newCaptured: null,
                newCapYear: null,
                newRemark: ''
            };
        },
        computed: {
            hasNext() {
                return this.getNextMessier() !== null;
            },
            hasPrevious() {
                return this.getPreviousMessier() !== null;
            }
        },
        mounted() {
            this.fetchMessierDetail();
        },
        watch: {
            id() {
                this.fetchMessierDetail();
            }
        },
        methods: {
            fetchMessierDetail() {
                const messier = this.messierObjects.find(m => m.Messier === this.id);
                if (messier) {
                    this.messier = messier;
                    this.atlasImagePath = this.getAtlasImagePath(messier.Messier);
                    this.roroImagePath = this.getRoroImagePath(messier.Messier);
                }
            },
            updateAnnotation() {
                const updatedAnnotation = {
                    Captured: this.newCaptured,
                    CapYear: this.newCapYear,
                    Remarks: this.newRemark
                };
                axios.post(`http://localhost:5000/api/messier/${this.id}`, updatedAnnotation)
                .then(response => {
                    this.messier = response.data;
                })
                .catch(error => {
                    console.error("Error updating annotation:", error);
                });
            },
            getNextMessier() {
                const currentIndex = this.messierObjects.findIndex(m => m.Messier === this.messier.Messier);
                return currentIndex >= 0 && currentIndex < this.messierObjects.length - 1 ? this.messierObjects[currentIndex + 1] : null;
            },
            getPreviousMessier() {
                const currentIndex = this.messierObjects.findIndex(m => m.Messier === this.messier.Messier);
                return currentIndex > 0 ? this.messierObjects[currentIndex - 1] : null;
            },
            goToNextMessier() {
                const nextMessier = this.getNextMessier();
                if (nextMessier) {
                    this.$router.push({ name: 'MessierDetail', params: { id: nextMessier.Messier } });
                }
            },
            goToPreviousMessier() {
                const previousMessier = this.getPreviousMessier();
                if (previousMessier) {
                    this.$router.push({ name: 'MessierDetail', params: { id: previousMessier.Messier } });
                }
            },    
            getAtlasImagePath(messierNumber) {
                const images = require.context('@/assets/atlas', false, /\.jpg$/);
                try {
                    return images(`./${messierNumber}.jpg`);
                } catch (e) {
                    return null;
                }
            },
            getRoroImagePath(messierNumber) {
                const images = require.context('@/assets/roro', false, /\.jpg$/);
                try {
                    return images(`./${messierNumber}.jpg`);
                } catch (e) {
                    return null;
                }
            }
        }
    };
</script>

<style>
    .images {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .images img {
        width: 100%;
        max-width: 600px;
        margin: 10px 0;
    }
    .annotations {
        margin-top: 20px;
    }
    .annotations textarea {
        width: 100%;
        height: 100px;
        margin-top: 10px;
    }
    .annotations input {
        width: 100%;
        margin-top: 10px;
    }
    .annotations button {
        margin-top: 10px;
    }
</style>

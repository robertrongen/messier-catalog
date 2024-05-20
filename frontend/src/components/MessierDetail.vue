<!-- frontend/src/components/MessierDetail.vue -->
<template>
    <div class="p-4 flex flex-wrap">
        <!-- Left Box: Details Table -->
        <div class="w-full md:w-1/2 md:pr-4">
            <h2 class="text-2xl font-bold mb-4">Messier Object {{ messier.Messier }}</h2>
            <table class="table-auto w-full text-left border-collapse border border-gray-200 dark:border-gray-700 mb-4">
                <tbody>
                    <tr class="border-t border-gray-200 dark:border-gray-700">
                        <td class="py-2 px-4 font-bold">NGC</td>
                        <td class="py-2 px-4">{{ messier.NGC }}</td>
                    </tr>
                    <tr class="border-t border-gray-200 dark:border-gray-700">
                        <td class="py-2 px-4 font-bold">Name</td>
                        <td class="py-2 px-4">{{ messier.Name }}</td>
                    </tr>
                    <tr class="border-t border-gray-200 dark:border-gray-700">
                        <td class="py-2 px-4 font-bold">Type</td>
                        <td class="py-2 px-4">{{ messier.Type }}</td>
                    </tr>
                    <tr class="border-t border-gray-200 dark:border-gray-700">
                        <td class="py-2 px-4 font-bold">Season</td>
                        <td class="py-2 px-4">{{ messier.Season }}</td>
                    </tr>
                    <tr class="border-t border-gray-200 dark:border-gray-700">
                        <td class="py-2 px-4 font-bold">Magnitude</td>
                        <td class="py-2 px-4">{{ messier.Magnitude }}</td>
                    </tr>
                    <tr class="border-t border-gray-200 dark:border-gray-700">
                        <td class="py-2 px-4 font-bold">Constellation</td>
                        <td class="py-2 px-4">{{ messier.Constellation }}</td>
                    </tr>
                    <tr class="border-t border-gray-200 dark:border-gray-700">
                        <td class="py-2 px-4 font-bold">RA</td>
                        <td class="py-2 px-4">{{ messier.RA }}</td>
                    </tr>
                    <tr class="border-t border-gray-200 dark:border-gray-700">
                        <td class="py-2 px-4 font-bold">Dec</td>
                        <td class="py-2 px-4">{{ messier.Dec }}</td>
                    </tr>
                    <tr class="border-t border-gray-200 dark:border-gray-700">
                        <td class="py-2 px-4 font-bold">Distance</td>
                        <td class="py-2 px-4">{{ messier.Distance }}</td>
                    </tr>
                    <tr class="border-t border-gray-200 dark:border-gray-700">
                        <td class="py-2 px-4 font-bold">Size</td>
                        <td class="py-2 px-4">{{ messier.Size }}</td>
                    </tr>
                    <tr class="border-t border-gray-200 dark:border-gray-700">
                        <td class="py-2 px-4 font-bold">Discoverer</td>
                        <td class="py-2 px-4">{{ messier.Discoverer }}</td>
                    </tr>
                    <tr class="border-t border-gray-200 dark:border-gray-700">
                        <td class="py-2 px-4 font-bold">Year</td>
                        <td class="py-2 px-4">{{ messier.Year }}</td>
                    </tr>
                    <tr class="border-t border-gray-200 dark:border-gray-700">
                        <td class="py-2 px-4 font-bold">Captured</td>
                        <td class="py-2 px-4">{{ messier.Captured }}</td>
                    </tr>
                    <tr class="border-t border-gray-200 dark:border-gray-700">
                        <td class="py-2 px-4 font-bold">Capture Year</td>
                        <td class="py-2 px-4">{{ messier.CapYear }}</td>
                    </tr>
                    <tr class="border-t border-gray-200 dark:border-gray-700">
                        <td class="py-2 px-4 font-bold">Remarks</td>
                        <td class="py-2 px-4">{{ messier.Remarks }}</td>
                    </tr>
                </tbody>
            </table>
            <div class="mt-4 flex justify-between">
                <button @click="goToPreviousMessier" :disabled="!hasPrevious" class="btn">
                    Previous
                </button>
                <button @click="goToNextMessier" :disabled="!hasNext" class="btn">
                    Next
                </button>
            </div>
            <div class="annotations mt-4 md:mt-0 w-full">
                <h3 class="text-xl font-bold mb-2">Add/Edit Annotation</h3>
                <input type="number" v-model="newCaptured" placeholder="Captured (0 or 1)"
                    class="form-input mt-1 block w-full" />
                <input type="number" v-model="newCapYear" placeholder="Capture Year"
                    class="form-input mt-1 block w-full" />
                <textarea v-model="newRemark" placeholder="Add annotation content..."
                    class="form-textarea mt-1 block w-full"></textarea>
                <button @click="updateAnnotation" class="btn mt-4">Save Annotation</button>
            </div>
        </div>
        <!-- Right Box: Atlas Image -->
        <div class="w-full md:w-1/2 md:pl-4 flex flex-col items-center">
            <div class="images mt-8 w-full">
                <img :src="atlasImagePath" alt="atlas Image" v-if="atlasImagePath" class="w-full mb-4" />
            </div>
        </div>
    </div>
    <div class="w-full md:w-1/2 md:pl-4 flex flex-col items-center">
        <div class="images mt-8 w-full">
            <img :src="roroImagePath" alt="roro Image" v-if="roroImagePath" class="w-full" />
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

.btn {
    @apply py-2 px-4 m-2 cursor-pointer transition-colors duration-300;
}

.dark .btn {
    @apply bg-gray-700 text-white hover:bg-gray-600;
}

.btn {
    @apply bg-gray-200 text-gray-900 hover:bg-gray-300;
}
</style>

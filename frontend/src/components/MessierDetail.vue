<!-- frontend/src/components/MessierDetail.vue -->
<template>
    <div class="mt-4 flex justify-between">
        <button @click="goToPreviousMessier" :disabled="!hasPrevious" class="btn">
            Previous
        </button>
        <button @click="goToNextMessier" :disabled="!hasNext" class="btn">
            Next
        </button>
    </div>
    <h2 class="text-2xl font-bold mb-4">Messier Object {{ messier.Messier }}</h2>
    <div class="p-4 flex flex-wrap">
        <!-- Left Box: Details Table -->
        <div class="w-full md:w-1/3 md:pr-4">
            <div class="annotations mt-4 md:mt-0 w-full">
                <h3 class="text-xl font-bold mb-2">Add/Edit Annotation</h3>
                <input type="number" v-model="newCaptured" placeholder="Captured (0 or 1)"
                    class="form-input mt-1 block w-full" />
                <input type="number" v-model="newCapYear" placeholder="Capture Year"
                    class="form-input mt-1 block w-full" />
                <input type="number" v-model="newPlanned" placeholder="Planned" class="form-input mt-1 block w-full" />
                <textarea v-model="newRemark" placeholder="Add annotation content..."
                    class="form-textarea mt-1 block w-full"></textarea>
                <button @click="updateAnnotation" class="btn mt-4">Save Annotation</button>
                <img v-if="annotation.image_filename"
                    :src="`${process.env.VUE_APP_API_BASE_URL}/static/uploads/${annotation.image_filename}`"
                    alt="Annotation Image" class="mt-2" />
                    <input type="file" @change="uploadThumbnail">
                <button @click="uploadImage"><em>Upload Thumbnail (max 150 x 150 px, must be square)</em></button>
                <input type="file" @change="uploadImage">
                <button @click="uploadImage">Upload Image (max width and height: 1600 px)</button>
            </div>
            <table class="table-auto w-full text-left border-collapse border border-gray-200 dark:border-gray-700 mb-4">
                <tbody>
                    <tr class="border-t border-gray-200 dark:border-gray-700">
                        <td class="py-2 px-4 font-bold">Captured</td>
                        <td class="py-2 px-4">{{ messier.Captured ? 'Yes' : 'No' }}</td>
                    </tr>
                    <tr class="border-t border-gray-200 dark:border-gray-700">
                        <td class="py-2 px-4 font-bold">Capture Year</td>
                        <td class="py-2 px-4">{{ messier.CapYear }}</td>
                    </tr>
                    <tr class="border-t border-gray-200 dark:border-gray-700">
                        <td class="py-2 px-4 font-bold">Planned?</td>
                        <td class="py-2 px-4">{{ messier.Planned ? 'Yes' : 'No' }}</td>
                    </tr>
                    <tr class="border-t border-gray-200 dark:border-gray-700">
                        <td class="py-2 px-4 font-bold">Remarks</td>
                        <td class="py-2 px-4">{{ messier.Remarks }}</td>
                    </tr>
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
                </tbody>
            </table>
        </div>

        <!-- Right Box: Atlas Image -->
        <div class="w-full md:w-2/3 md:pr-4">
            <img :src="posImagePath" alt="pos Image" v-if="posImagePath && !roroImagePath" class="w-full"
                style="max-width: 180px; max-height: 180px; margin: 0 auto;" />
            <div class="images mt-8 w-full">
                <img :src="roroImagePath" alt="roro Image" v-if="roroImagePath" class="w-full" />
                <img :src="amImagePath" alt="roro Image" v-if="amImagePath" class="w-full" />
                <img :src="atlasImagePath" alt="atlas Image" v-if="atlasImagePath" class="w-full mb-4" />
            </div>
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
            newPlanned: null,
            newRemark: '',
            annotation: {},
            image: null,
            posImagePath: null,
            roroThImagePath: null,
            amImagePath: null
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
        this.fetchAnnotation();
    },
    watch: {
        id() {
            this.fetchMessierDetail();
            this.fetchAnnotation();
        }
    },
    methods: {
        fetchMessierDetail() {
            const messier = this.messierObjects.find(m => m.Messier === this.id);
            if (messier) {
                this.messier = messier;
                this.atlasImagePath = this.getAtlasImagePath(messier.Messier);
                this.roroThImagePath = this.getRoroThImagePath(messier.Messier);
                this.roroImagePath = this.getRoroImagePath(messier.Messier);
                this.posImagePath = this.getPosImagePath(messier.Messier);

                this.amImagePath = this.getAmImagePath(messier.Messier);
            }
        },
        fetchAnnotation() {
            axios.get(`${process.env.VUE_APP_API_BASE_URL}/annotations`, {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('token')}`
                }
            })
                .then(response => {
                    this.annotation = response.data.find(a => a.messier_id === parseInt(this.id));
                    if (this.annotation) {
                        this.newCaptured = this.annotation.captured;
                        this.newCapYear = this.annotation.cap_year;
                        this.newPlanned = this.annotation.planned;
                        this.newRemark = this.annotation.remarks;
                    } else {
                        this.resetAnnotationForm();
                    }
                })
                .catch(error => {
                    console.error("Error fetching annotation:", error);
                });
        },
        updateAnnotation() {
            const formData = new FormData();
            formData.append('messier_id', this.id);
            formData.append('captured', this.newCaptured);
            formData.append('cap_year', this.newCapYear);
            formData.append('remarks', this.newRemark);
            formData.append('planned', this.newPlanned);
            if (this.image) {
                formData.append('file', this.image);
            }

            axios.post(`${process.env.VUE_APP_API_BASE_URL}/annotations`, formData, {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('token')}`,
                    'Content-Type': 'multipart/form-data'
                }
            })
                .then(response => {
                    this.annotation = response.data;
                    this.resetAnnotationForm();
                })
                .catch(error => {
                    console.error('Error updating annotation:', error);
                });
        },
        onFileChange(event) {
            this.image = event.target.files[0];
        },
        resetAnnotationForm() {
            this.newCaptured = false;
            this.newCapYear = null;
            this.newPlanned = false;
            this.newRemark = '';
            this.image = null;
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
        getRoroThImagePath(messierNumber) {
            const images = require.context('@/assets/roro_th', false, /\.jpg$/);
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
        },
        getPosImagePath(messierNumber) {
            const images = require.context('@/assets/pos', false, /\.jpg$/);
            try {
                return images(`./${messierNumber}.jpg`);
            } catch (e) {
                return null;
            }
        },
        getAmImagePath(messierNumber) {
            const images = require.context('@/assets/amateur', false, /\.jpg$/);
            try {
                return images(`./${messierNumber}.jpg`);
            } catch (e) {
                return null;
            }
        }
    }
};
</script>

<style scoped>
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

<!-- frontend/src/components/AnnotationComponent.vue -->
<template>
    <div class="p-4">
        <h2 class="text-2xl font-bold mb-4">Annotations</h2>
        <form @submit.prevent="saveAnnotation">
            <div class="mb-4">
                <label class="block text-sm font-medium text-gray-700">Messier ID</label>
                <input v-model="messierId" type="number" class="form-input mt-1 block w-full" />
            </div>
            <div class="mb-4">
                <label class="block text-sm font-medium text-gray-700">Captured</label>
                <input v-model="captured" type="checkbox" class="form-checkbox mt-1" />
            </div>
            <div class="mb-4">
                <label class="block text-sm font-medium text-gray-700">Capture Year</label>
                <input v-model="capYear" type="number" class="form-input mt-1 block w-full" />
            </div>
            <div class="mb-4">
                <label class="block text-sm font-medium text-gray-700">Remarks</label>
                <textarea v-model="remarks" class="form-textarea mt-1 block w-full"></textarea>
            </div>
            <div class="mb-4">
                <label class="block text-sm font-medium text-gray-700">Planned</label>
                <input v-model="planned" type="checkbox" class="form-checkbox mt-1" />
            </div>
            <div class="mb-4">
                <label class="block text-sm font-medium text-gray-700">Upload Image</label>
                <input type="file" @change="onFileChange" class="form-input mt-1 block w-full" />
            </div>
            <button type="submit" class="px-4 py-2 bg-blue-500 text-white rounded">Save Annotation</button>
        </form>
        <div class="mt-8">
            <h3 class="text-xl font-bold mb-2">Your Annotations</h3>
            <ul>
                <li v-for="annotation in annotations" :key="annotation.id">
                    <div>
                        <p>Messier ID: {{ annotation.messier_id }}</p>
                        <p>Captured: {{ annotation.captured }}</p>
                        <p>Capture Year: {{ annotation.cap_year }}</p>
                        <p>Remarks: {{ annotation.remarks }}</p>
                        <p>Planned: {{ annotation.planned }}</p>
                        <img v-if="annotation.image_filename"
                            :src="`${process.env.VUE_APP_API_BASE_URL}/static/uploads/${annotation.image_filename}`"
                            alt="Annotation Image" class="mt-2" />
                    </div>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            messierId: null,
            captured: false,
            capYear: null,
            remarks: '',
            planned: false,
            image: null,
            annotations: []
        }
    },
    created() {
        this.fetchAnnotations();
    },
    methods: {
        fetchAnnotations() {
            axios.get(`${process.env.VUE_APP_API_BASE_URL}/annotations`, {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('token')}`
                }
            })
                .then(response => {
                    this.annotations = response.data;
                })
                .catch(error => {
                    console.error('Error fetching annotations:', error);
                });
        },
        saveAnnotation() {
            const formData = new FormData();
            formData.append('messier_id', this.messierId);
            formData.append('captured', this.captured);
            formData.append('cap_year', this.capYear);
            formData.append('remarks', this.remarks);
            formData.append('planned', this.planned);
            if (this.image) {
                formData.append('file', this.image);
            }

            axios.post(`${process.env
                .VUE_APP_API_BASE_URL}/annotations`, formData, {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('token')}`,
                    'Content-Type': 'multipart/form-data'
                }
            })
                .then(response => {
                    this.annotations.push(response.data);
                    this.resetForm();
                })
                .catch(error => {
                    console.error('Error saving annotation:', error);
                });
        },
        onFileChange(event) {
            this.image = event.target.files[0];
        },
        resetForm() {
            this.messierId = null;
            this.captured = false;
            this.capYear = null;
            this.remarks = '';
            this.planned = false;
            this.image = null;
        }
    }
}
</script>

<style scoped>
.form-input,
.form-textarea,
.form-checkbox {
    @apply border-gray-300 rounded-md shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50;
}
</style>

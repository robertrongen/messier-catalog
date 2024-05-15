<template>
    <div class="image-grid">
        <div v-for="object in messierObjects" :key="object.Messier" class="image-item">
            <img :src="getImagePath(object)" :alt="`Messier ${object.Messier}`" />
            <div class="caption">{{ object.Name }}</div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'MessiersBox',
    props: {
        messierObjects: Array
    },
    methods: {
        getImagePath(object) {
            try {
                return require(`@/assets/${object.Captured ? 'pos' : 'neg'}/${object.Messier}.jpg`);
            } catch (e) {
                console.error("Failed to load image", e);
                return '';
            }
        }
    }
}
</script>

<style>
.image-grid {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}
.image-item {
    margin: 5px;
}
.image-item img {
    width: 180px;  /* Or adjust based on your CSS Grid setup */
    height: 180px;
}
.caption {
    text-align: center;
}
</style>  
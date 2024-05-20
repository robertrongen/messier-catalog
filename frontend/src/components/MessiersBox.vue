<!-- frontend/src/components/MessiersBox.vue -->
<template>
    <div class="grid grid-cols-2 sm:grid-cols-4 md:grid-cols-6 lg:grid-cols-8 gap-4 p-4">
        <div v-for="object in messierObjects" :key="object.Messier" class="relative"
            @mouseover="hoveredImage = object.Messier" @mouseleave="hoveredImage = null">
            <div class="imgtitle">
                <strong>{{ object.Messier }}</strong>
                <br />
                {{ object.Constellation }}
            </div>
            <router-link :to="{ name: 'MessierDetail', params: { id: object.Messier } }">
                <img :src="getImagePath(object)" :alt="`Messier ${object.Messier}`" :id="`img-${object.Messier}`" />
            </router-link>
            <div class="imgcaption">
                {{ object.Type }}
                <br />
                {{ object.Season }}
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "MessiersBox",
    props: {
        messierObjects: Array,
    },
    data() {
        return {
            hoveredImage: null,
        };
    },
    methods: {
        getImagePath(object) {
            const isHovered = this.hoveredImage === object.Messier;
            const type = object.Captured ? "roro" : "neg";
            const hoverType = object.Captured ? "pos" : "pos";
            return isHovered
                ? require(`@/assets/${hoverType}/${object.Messier}.jpg`)
                : require(`@/assets/${type}/${object.Messier}.jpg`);
        },
    },
};
</script>

<style>
.imgtitle, .imgcaption {
    padding: 0.5rem;
    font-size: 0.9rem;
}
</style>

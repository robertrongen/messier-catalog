<!-- frontend/src/components/MessiersBox.vue -->
<template>
    <div class="image-grid">
        <div 
            v-for="object in messierObjects" 
            :key="object.Messier"
            class="image-item"
            @mouseover="hoveredImage = object.Messier"
            @mouseleave="hoveredImage = null"
        >
            <div class="imgtitle">
                {{ object.Messier }}
                <br/>
                {{ object.Constellation }}
            </div>
            <router-link :to="{ name: 'MessierDetail', params: { id: object.Messier } }">
                <img 
                    :src="getImagePath(object)" 
                    :alt="`Messier ${object.Messier}`" 
                    :id="`img-${object.Messier}`"
                />
            </router-link>
            <div class="caption">
                {{ object.Type }}
                <br/>
                {{ object.Season }}
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'MessiersBox',
        props: {
            messierObjects: Array
        },
        data() {
            return {
            hoveredImage: null
            };
        },
        methods: {
            getImagePath(object) {
                const isHovered = this.hoveredImage === object.Messier;
                const type = object.Captured ? 'roro' : 'neg';
                const hoverType = object.Captured ? 'pos' : 'pos';
                return isHovered 
                    ? require(`@/assets/${hoverType}/${object.Messier}.jpg`) 
                    : require(`@/assets/${type}/${object.Messier}.jpg`);
            },
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
        padding: 5px; 
    }
    .image-item img {
        width: 100%; /* Make image fill the container */
        height: auto; /* Keep the aspect ratio */
    }
    .caption {
        text-align: center;
    }
</style>
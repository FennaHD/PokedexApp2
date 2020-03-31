<template>
  <div>
    <div v-if="favorites.length === 0" class="empty">
      No favorite Pokemons... Yet! Go get some!
    </div>
    <div v-else>
      <FavoritesComponent :favorites="favorites"/>
    </div>
  </div>
</template>

<script>
import FavoritesComponent from '../components/FavoritesComponent.vue'

export default {
  name: 'Favorites',
  data() {
    return {
      favorites: this.$root.$data.favorites
    }
  },
  components: {
    FavoritesComponent
  }
}
</script>

<style scoped>
.empty {
  margin: 40px 0px;
  font-size: 40px;
}
</style>

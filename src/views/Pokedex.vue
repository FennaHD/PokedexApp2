<template>
  <div>
    <div class="wrapper mt-5">
      <div class="search">
        <form class="pure-form">
          <i class="fas fa-search"></i><input v-model="searchText" placeholder="Enter Name"/>
        </form>
      </div>
    </div>
    <PokedexComponent :pokemons="pokemons"/>
  </div>
</template>

<script>
// @ is an alias to /src
import PokedexComponent from '../components/PokedexComponent.vue'

export default {
  name: 'Pokedex',
  data() {
    return {
      searchText: '',
    }
  },
  components: {
    PokedexComponent
  },
  computed: {
    pokemons() {
      return this.$root.$data.pokemons.filter(pokemon => pokemon.name.toLowerCase().search(this.searchText.toLowerCase()) >= 0);
    }
  }
}
</script>

<style scoped>
.wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 20px;
}

.search {
  border: 1px solid #ccc;
  border-radius: 4px;
  width: 50%;
}

form {
  display: table;
  width: 100%;
}

i {
  display: table-cell;
  padding-left: 10px;
  width: 1px;
}

input {
  display: table-cell;
  font-size: 20px;
  border: none !important;
  box-shadow: none !important;
  width: 100%;
  height: 40px;
}
</style>

<template>
  <div>
    <div>
      <div class="pure-menu pure-menu-horizontal mt-5">
        <ul class="pure-menu-list">
          <li class="pure-menu-item"><a id="Normal" @click="select('Normal')" href="#" class="btn btn-outline-primary">Normal</a></li>
          <li class="pure-menu-item"><a id="Grass" @click="select('Grass')" href="#" class="btn btn-outline-primary">Grass</a></li>
          <li class="pure-menu-item"><a id="Fire" @click="select('Fire')" href="#" class="btn btn-outline-primary">Fire</a></li>
          <li class="pure-menu-item"><a id="Water" @click="select('Water')" href="#" class="btn btn-outline-primary">Water</a></li>
          <li class="pure-menu-item"><a id="Fighting" @click="select('Fighting')" href="#" class="btn btn-outline-primary">Fighting</a></li>
          <li class="pure-menu-item"><a id="Flying" @click="select('Flying')" href="#" class="btn btn-outline-primary">Flying</a></li>
          <li class="pure-menu-item"><a id="Poison" @click="select('Poison')" href="#" class="btn btn-outline-primary">Poison</a></li>
          <li class="pure-menu-item"><a id="Ground" @click="select('Ground')" href="#" class="btn btn-outline-primary">Ground</a></li>
          <li class="pure-menu-item"><a id="Rock" @click="select('Rock')" href="#" class="btn btn-outline-primary">Rock</a></li>
          <li class="pure-menu-item"><a id="Bug" @click="select('Bug')" href="#" class="btn btn-outline-primary">Bug</a></li>
          <li class="pure-menu-item"><a id="Ghost" @click="select('Ghost')" href="#" class="btn btn-outline-primary">Ghost</a></li>
          <li class="pure-menu-item"><a id="Electric" @click="select('Electric')" href="#" class="btn btn-outline-primary">Electric</a></li>
          <li class="pure-menu-item"><a id="Psychic" @click="select('Psychic')" href="#" class="btn btn-outline-primary">Psychic</a></li>
          <li class="pure-menu-item"><a id="Ice" @click="select('Ice')" href="#" class="btn btn-outline-primary">Ice</a></li>
          <li class="pure-menu-item"><a id="Dragon" @click="select('Dragon')" href="#" class="btn btn-outline-primary">Dragon</a></li>
          <li class="pure-menu-item"><a id="Dark" @click="select('Dark')" href="#" class="btn btn-outline-primary">Dark</a></li>
          <li class="pure-menu-item"><a id="Steel" @click="select('Steel')" href="#" class="btn btn-outline-primary">Steel</a></li>
          <li class="pure-menu-item"><a id="Fairy" @click="select('Fairy')" href="#" class="btn btn-outline-primary">Fairy</a></li>
        </ul>
      </div>
    </div>
    <div v-if="pokemons.length === 0" class="empty">
      No pokemons fit that criteria. Keep exploring!
    </div>
    <div v-else>
      <PokedexComponent :pokemons="pokemons"/>
    </div>
  </div>
</template>

<script>
import PokedexComponent from '../components/PokedexComponent.vue'

export default {
  name: "ByType",
  components: {
    PokedexComponent
  },
  data() {
    return {
      types: []
    }
  },
  computed: {
    pokemons() {
      return this.$root.$data.pokemons.filter(pokemon => this.types.every(type => pokemon.types.includes(type)));
    }
  },
  methods: {
    select(type) {
      if (this.types.includes(type)) {
          document.getElementById(type).classList.remove("active");
          this.types.splice(this.types.indexOf(type));
      } else {
        document.getElementById(type).classList.add("active");
        this.types.push(type);
      }
    }
  }
}


</script>

<style scoped>

.pure-menu {
  display: flex;
  justify-content: center;
  width: 100%;
}

.pure-menu-list {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    flex-direction: row;
    width: 70%;
}

li {
  margin: 5px;
  display: flex;
  list-style-position: outside;
  height: 50px;
}
</style>

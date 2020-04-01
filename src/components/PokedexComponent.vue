<template>
  <div class="wrapper">
    <div class="container">
      <div class="pokemons">
        <div v-for="(pokemon, id) in pokemons" :key="id" class="indiv-pokemon">
          <img :src="pokemon.little_image">
          <p>#{{pokemon.id}}<br>{{pokemon.name}}</p>
          <div @click="addToFavorites(pokemon)">
            <div v-if="favorites.includes(pokemon)">
              <button type="button" class="btn btn-danger">Remove</button>
            </div>
            <div v-else>
              <button type="button" class="btn btn-success">+ Favorite</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "PokedexComponent",
  props: {
    pokemons: Array
  },
  data() {
    return {
      favorites: this.$root.$data.favorites
    }
  },
  methods: {
    addToFavorites(pokemon) {
      if (this.favorites.includes(pokemon)) {
        console.log("removed " + pokemon.name);
        this.favorites.splice(this.favorites.indexOf(pokemon), 1);
        console.log("Favorite count: " + this.favorites.length)
      } else {
        console.log("added " + pokemon.name);
        this.favorites.push(pokemon);
      }
    }
  }
}
</script>

<style scoped>

  .container {
    display: flex;
    width: 100%;
    justify-content: center;
  }

  .pokemons {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
  }

  .indiv-pokemon {
    margin: 10px;
    border: 1px solid grey;
    border-radius: 15px;
    cursor: pointer;
    width: 150px;
    background-color: #f0e9e9;
  }

  .indiv-pokemon:hover {
    color: white;
    background-color: #30a7d7;
  }

  p {
    margin-top: 0px;
    font-size: 20px;
    font-weight: bold;
  }

  img {
    margin-top: 15px;
    width: 120px;
  }

  button {
    border-radius: 12px;
    margin-bottom: 10px;
  }

  @media only screen and (max-width: 991px) {
    .container {
      width: 75%;
    }
  }

  @media only screen and (max-width: 870px) {
    .container {
      width: 95%;
    }
  }

  @media only screen and (max-width: 790px) {
    .container {
      width: 95%;
    }
  }
</style>

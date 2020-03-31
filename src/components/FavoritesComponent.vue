<template>
  <div class="content-wrapper">
    <div v-for="pokemon in favorites" :key="pokemon.id" class="content-container">
      <div class="row center main-name">
        <h1><span id="pokemon-title-name">{{pokemon.name}} </span><span id="pokemon-title-id">#{{pokemon.id}}</span></h1>
      </div>
      <div class="row center">
        <div class="pokemon-image-container">
          <img id="pokemon-image" :src="pokemon.large_image">
        </div>

        <div class="stats-container">
          <div class="row">
            <div class="stat-box">
              <span class="stat-name">Height: </span><span id="height">{{pokemon.feet}}' {{pokemon.inches}}"</span>
            </div>
          </div>
          <div class="row">
            <div class="stat-box">
              <span class="stat-name">Weight: </span><span id="weight">{{pokemon.weight}} lbs</span>
            </div>
          </div>
          <div class="row type">
            <div class="stat-box">
              <span class="stat-name">Type: </span><span id="types">{{pokemon.types.join(", ")}}</span>
            </div>
          </div>
          <br>
          <div @click="remove(pokemon)" class="remove-wrapper">
            <div class="remove-container btn btn-danger btn-lg">
              <span><svg class="bi bi-x-circle" width="1em" height="1em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" d="M8 15A7 7 0 108 1a7 7 0 000 14zm0 1A8 8 0 108 0a8 8 0 000 16z" clip-rule="evenodd"/>
                <path fill-rule="evenodd" d="M11.854 4.146a.5.5 0 010 .708l-7 7a.5.5 0 01-.708-.708l7-7a.5.5 0 01.708 0z" clip-rule="evenodd"/>
                <path fill-rule="evenodd" d="M4.146 4.146a.5.5 0 000 .708l7 7a.5.5 0 00.708-.708l-7-7a.5.5 0 00-.708 0z" clip-rule="evenodd"/></svg>
                Remove</span>
            </div>
          </div>
        </div>
      </div>
      <hr>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FavoritesComponent',
  props: {
    favorites: Array
  },
  methods: {
    remove(pokemon) {
      this.favorites.splice(this.favorites.indexOf(pokemon), 1);
    }
  }
}
</script>

<style scoped>
h1 {
  margin-bottom: 0px;
}

.remove-wrapper {
  display: flex;
  justify-content: center;
}

.remove-container {
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 30px;
  width: 70%;
  border-radius: 12px;
}
hr {
  border-top: 1px solid #8c8b8b;
}

.content-wrapper {
  margin-top: 15px;
  width: 100%;
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
}

.content-container {
  width: 65%;
  background-color: white;
}

.pokemon-image-container {
  width: 60%;
}

.stats-container {
  border-radius: 25px;
  background-color: #30a7d7;
  width: 40%;
  font-size: 27px;
  line-height: 45px;
  padding: 30px 8px;
}

@media only screen and (max-width: 991px) {
  .content-container {
    width: 75%;
  }
}

@media only screen and (max-width: 870px) {
  .content-container {
    width: 85%;
  }
}

@media only screen and (max-width: 790px) {
  .content-container {
    width: 95%;
  }
}

@media only screen and (max-width: 715px) {
  .pokemon-image-container {
    width: 80%;
  }

  .stats-container {
    min-width: 330px;
  }
}

@media only screen and (max-width: 685px) {
  .previous-span {
    font-size: 20px;
  }

  .next-span {
    font-size: 20px;
  }
}

@media only screen and (max-width: 580px) {
  .content-container {
    width: 98%;
  }

  .col {
    padding: 0px;
  }

  .previous {
    padding: 0px 10px;
    height: 50px;
  }

  .previous-span {
    font-size: 15px;
    margin-left: 10px;
  }

  .next {
    padding: 0px 10px;
    height: 50px;
  }

  .next-span {
    font-size: 15px;
    margin-right: 10px;
  }
}

@media only screen and (max-width: 450px) {
  .previous-span {
    width: 100%;
    font-size: 17px;
    display: flex;
    justify-content: center;
    flex-direction: column;
  }

  .next-span {
    width: 100%;
    font-size: 17px;
    display: flex;
    justify-content: center;
    flex-direction: column-reverse;
  }
}

@media only screen and (max-width: 380px) {
  .previous-span {
    font-size: 13px;
  }

  #previous-id {
    margin-top: 0px;
  }

  .next-span {
    font-size: 13px;
  }
}

.row {
  margin: 0;
}

.center {
  display: flex;
  justify-content: center;
  align-items: center;
}

.space-between {
  justify-content: space-between;
}

#previous-id {
  color: white;
}

.previous:hover {
  background-color: #30a7d7;
}

.next:hover {
  background-color: #30a7d7;
}

#next-id {
  color: white;
}

.main-name {
  text-align: center;
}

#pokemon-title-id {
  color: #a4a4a4;
}

#pokemon-image {
  width: 100%;

}

#sprites {
  margin: 0 auto;
}

.loading {
  margin-top: 15px !important;
  margin-bottom: 15px !important;
}

.stat-box {
  margin: auto 15px auto 15px;
}

strong {
  font-weight: 900;
}

.stat-name {
  color: white;
}

.type {
  margin-bottom: 20px;
}

#pokedex {
  display: none;
}

.form-inline {
  display: flex;
  justify-content: center;
}

.alert {
  display: none;
}

.instructions {
  font-size: 15px !important;
}

.welcome {
  font-size: 20px;
  text-align: center;
}

</style>

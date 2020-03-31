import Vue from 'vue'
import App from './App.vue'
import router from './router'
import mock from './mock.js'

let data = {
  pokemons: mock,
  favorites: []
}

new Vue({
  router,
  data,
  render: h => h(App)
}).$mount('#app')

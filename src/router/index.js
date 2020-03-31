import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Pokedex from '../views/Pokedex.vue'
import ByType from '../views/ByType.vue'
import Favorites from '../views/Favorites.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/pokedex',
    name: 'Pokedex',
    component: Pokedex
  },
  {
    path: '/bytype',
    name: 'ByType',
    component: ByType
  },
  {
    path: '/favorites',
    name: 'Favorites',
    component: Favorites
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

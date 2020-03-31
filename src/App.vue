<template>
  <div id="app">
    <nav class="navbar navbar-dark bg-dark">
      <router-link to="/">Home</router-link>
      <router-link to="/pokedex">Pokedex</router-link>
      <router-link to="/bytype">By Type</router-link>
      <router-link to="/favorites">Favorites</router-link>
    </nav>
    <router-view/>

    <!-- Footer -->
      <footer class="page-footer font-small dark darken-3">
        <!-- Footer Elements -->
        <div class="footer-container">
          <!-- Grid row-->
          <div class="row">
            <!-- Grid column -->
            <div class="col-md-12 py-5">
              <div class="flex-center">
                <!-- Facebook -->
                <a class="fb-ic" href="https://www.facebook.com/fernando.maluenda" target="_blank">
                  <i class="fab fa-facebook-f fa-lg black-text mr-md-5 mr-sm-5 mr-4 fa-2x"> </i>
                </a>
                <!-- Twitter -->
                <a class="tw-ic" href="https://twitter.com/Pokemon?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor" target="_blank">
                  <i class="fab fa-twitter fa-lg black-text mr-md-5 mr-sm-5 mr-4 fa-2x"> </i>
                </a>
                <!--Linkedin -->
                <a class="li-ic" href="https://www.linkedin.com/in/fernando-maluenda-7a4a46158/" target="_blank">
                  <i class="fab fa-linkedin-in fa-lg black-text mr-md-5 mr-sm-5 mr-4 fa-2x"> </i>
                </a>
                <!--Instagram-->
                <a class="ins-ic" href="https://www.instagram.com/pokemon/?hl=en" target="_blank">
                  <i class="fab fa-instagram fa-lg black-text mr-md-5 mr-sm-5 mr-4 fa-2x"> </i>
                </a>
                <!-- Github -->
                <a class="gb-ic" href="https://github.com/FennaHD/PokedexApp" target="_blank">
                  <i class="fab fa-github fa-lg black-text mr-md-5 mr-sm-5 mr-4 fa-2x"></i>
                </a>
              </div>
            </div>
            <!-- Grid column -->
          </div>
          <!-- Grid row-->
        </div>
        <!-- Footer Elements -->
      </footer>
    <!-- Footer -->

  </div>
</template>

<style>
#app {
  font-family: 'Oxanium', cursive;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.navbar {
  padding: 8px 300px;
  margin-bottom: 30px
}

.navbar a {
  font-size: 20px;
  color: white;
}

.navbar a.router-link-exact-active {
  color: #007bff;
}

.page-footer a {
  color: #343a40;
}
</style>

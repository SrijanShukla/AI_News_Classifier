<template>
  <div>
    <nav class="navbar navbar-expand-lg bg-light">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">AI News Classifier</a>

        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">

            <li class="nav-item" style="margin-left:10in">
              <a class="nav-link" href="#" @click.prevent="logout()">Instructions</a>
            </li>

          </ul>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: 'NavBar',
  data() {
    return {
      summarytoggle: false,
    }
  },
  methods: {
    logout() {

      window.location = ('/home')

    }
  }
}
</script>


<style>

</style>

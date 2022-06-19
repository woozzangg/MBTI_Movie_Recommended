<template>
  <div id="app">

    <nav-bar></nav-bar>
    <body class="pt-5 pb-5 background">
      <router-view class="py-2 pb-5"></router-view>
    </body>
    
  </div>
</template>

<script>
  import NavBar from '@/components/NavBar.vue'

  import { mapActions } from 'vuex'

  export default {
    name: 'App',
    components: { NavBar },
    methods: {
      ...mapActions(['fetchCurrentUser'])
    },
    created() {
      this.fetchCurrentUser()
    }
  }
</script>

<style>

.background {
  /* color: #3ed4c2; */
  background-color: #ecfffb;
  padding-bottom: 100px;
  }
.mint{
  background-color: #12d3a9;
}
.choco{
  background-color: #563d34;

}
</style>

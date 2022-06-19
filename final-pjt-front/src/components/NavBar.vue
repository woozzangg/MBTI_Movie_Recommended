<template>
  <div class="fixed-top">
    <b-navbar toggleable="lg" type="light" class="mint font-weight-bold">
      <b-navbar-brand :to="{ name: 'home' }">
        <img src="@/assets/logo.png" width="32" alt="logo">
      </b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item :to="{ name: 'articles' }">Community</b-nav-item>
          <b-nav-item :to="{ name: 'movies' }">Movie</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-form>
            <b-form-input v-model=word size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
            <b-button :to="{ name: 'moviesSearch', params: { word } }" size="sm" class="my-2 my-sm-0 choco" type="submit" style="background-color: #563d34; color: #12d3a9; font-weight: bold;">Search</b-button>
          </b-nav-form>

          <b-nav-item :to="{ name: 'signup' }" v-if="!isLoggedIn">
            SignUp 
          </b-nav-item>
          <b-nav-item :to="{ name: 'login' }" v-if="!isLoggedIn">
            LogIn
          </b-nav-item>
          <b-nav-item-dropdown v-if="isLoggedIn" right>
            <!-- Using 'button-content' slot -->
            <template #button-content>
              <em>{{ currentUser.username }}</em>
            </template>
            <b-dropdown-item :to="{ name: 'profile', params: { username } }">Profile</b-dropdown-item>
            <b-dropdown-item :to="{ name: 'logout' }">Log Out</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
  <!-- <b-nav tabs>
    <b-nav-item>
      <router-link :to="{ name: 'home' }">메인페이지</router-link>
    </b-nav-item>
    <b-nav-item>
      <router-link :to="{ name: 'articles' }">자게</router-link>
    </b-nav-item>
    <b-nav-item v-if="isLoggedIn">
      <router-link :to="{ name: 'articleNew' }">글쓰기</router-link>
    </b-nav-item>
  
    <div class="ml-auto d-flex">
      <b-nav-item v-if="!isLoggedIn">
        <router-link :to="{ name: 'signup' }">회원가입</router-link>
      </b-nav-item>
      <b-nav-item v-if="!isLoggedIn">
        <router-link :to="{ name: 'login' }">로그인</router-link>
      </b-nav-item>

      <b-nav-item v-if="isLoggedIn">
        <router-link :to="{ name: 'profile', params: { username } }">
          {{ currentUser.username }}
        </router-link>
      </b-nav-item>
      <b-nav-item v-if="isLoggedIn" right>
        <router-link :to="{ name: 'logout' }">로그아웃</router-link>
      </b-nav-item>
    </div>
  </b-nav> -->
</template>

<script>
  import { mapGetters } from 'vuex'

  export default {
    name: 'NavBar',
    data() {
      return {
        word: '',
      }
    },
    computed: {
      ...mapGetters(['isLoggedIn', 'currentUser']),
      username() {
        return this.currentUser.username ? this.currentUser.username : 'guest'
      },
    },
  }
</script>

<style>

</style>

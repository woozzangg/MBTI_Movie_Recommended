<template>
  <div class ="d-flex flex-column align-items-center">
    <!-- <h1>Login</h1> -->
    <account-error-list v-if="authError"></account-error-list>
    <form class ="login-form mb-5 mr-5  d-flex flex-column align-items-left" @submit.prevent="login(credentials)">
      <h2 class="mb-3">로그인</h2>
      <div class="mb-3">
        <!-- <label for="username" class="pr-2">아이디 : </label> -->
        <input class="w-100 login-input my-2" v-model="credentials.username" type="text" id="username" placeholder="ID" required />
      </div>
      <div class="mb-3">
        <!-- <label for="password" class="pr-2">비밀번호 : </label> -->
        <input class="w-100 login-input my-2" v-model="credentials.password" type="password" id="password" placeholder="Password" required />
      </div>
      <div>
        <button class="btn btn-lg btn-success my-3 mt-3" >Login</button>
      </div>
    </form>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'LoginView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password: '',
        }
      }
    },
  computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['login'])
    },
  }
</script>
<style>
.login-input {
  height: 50px;
}
.login-form {
  width: 500px;
  height: 370px;
  border-radius: 5px;
  border: 1px solid rgb(214, 214, 214);
  background-color: white;
  margin: 2rem;
  padding: 2rem;
}
</style>
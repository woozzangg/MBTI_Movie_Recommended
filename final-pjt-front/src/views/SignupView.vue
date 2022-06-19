<template>
  <div class ="  d-flex flex-column align-items-center">
    <!-- <h1>Signup</h1> -->

    <account-error-list v-if="authError"></account-error-list>

    <form class ="signup-form  d-flex flex-column align-items-left" @submit.prevent="signup(credentials)">
      <h2>회원가입</h2>
      <br>
      <div class="mb-3">
        <!-- <label for="username" class="pr-2">아이디 : </label> -->
        <input  v-model="credentials.username" type="text" id="username" placeholder="ID" required/>
      </div>
      <div class="mb-3">
        <!-- <label for="password1" class="pr-2">비밀번호 : </label> -->
        <input v-model="credentials.password1" type="password" id="password1" placeholder="Password" required />
      </div>
      <div class="mb-3">
        <!-- <label for="password2" class="pr-2">비밀번호 확인 :</label> -->
        <input v-model="credentials.password2" type="password" id="password2" placeholder="Password Confirmation" required />
      </div>
      <div>
        <select class="form-select form-select-lg mb-3" aria-label=".form-select-lg example">
          <option selected>당신의 성격은 어느 쪽에 가깝나요?</option>
          <option value="1">내향형(I)</option>
          <option value="2">외향형(E)</option>
        </select>
      </div>
      <div>
        <select class="form-select form-select-lg mb-3" aria-label=".form-select-lg example">
          <option selected>당신의 성격은 어느 쪽에 가깝나요?</option>
          <option value="1">직관형(N)</option>
          <option value="2">감각형(S)</option>
        </select>        
      </div>
      <div>
        <select class="form-select form-select-lg mb-3" aria-label=".form-select-lg example">
          <option selected>당신의 성격은 어느 쪽에 가깝나요?</option>
          <option value="1">감정형(F)</option>
          <option value="2">사고형(T)</option>
        </select>        
      </div>
      <div>
        <select class="form-select form-select-lg mb-3" aria-label=".form-select-lg example">
          <option selected>당신의 성격은 어느 쪽에 가깝나요?</option>
          <option value="1">인식형(P)</option>
          <option value="2">판단형(J)</option>
        </select>        
      </div>
      <br>
      <div>
        <button class="btn btn-success" >Signup</button>
      </div>
    </form>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'SignupView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password1: '',
          password2: '',
        }
      }
    },
    computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['signup'])
    },
  }
</script>

<style>
.signup-form {
  border: 1px solid #070a08;
  background-color: rgb(241, 240, 238);
  margin: 2rem;
  padding: 2rem;
}
</style>

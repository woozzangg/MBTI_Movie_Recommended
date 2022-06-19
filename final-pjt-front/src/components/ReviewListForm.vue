<template>
  <b-card>
    <h3 class="mb-4">댓글 작성</h3>
    <form @submit.prevent="onSubmit">
      <textarea class="form-control form-control-lg mb-3" v-model="content" type="text" id="content" placeholder="내용" rows="3" required></textarea>

      <div class="star-rating space-x-4 mx-2 my-3">
        <input type="radio" id="5-stars" name="rating" value="5" v-model="rank"/>
        <label for="5-stars" class="star pr-4">♥</label>
        <input type="radio" id="4-stars" name="rating" value="4" v-model="rank"/>
        <label for="4-stars" class="star">♥</label>
        <input type="radio" id="3-stars" name="rating" value="3" v-model="rank"/>
        <label for="3-stars" class="star">♥</label>
        <input type="radio" id="2-stars" name="rating" value="2" v-model="rank"/>
        <label for="2-stars" class="star">♥</label>
        <input type="radio" id="1-star" name="rating" value="1" v-model="rank" />
        <label for="1-star" class="star">♥</label>
      </div>
      <div>
        <button>리뷰 작성</button>
      </div>
    </form>
  </b-card>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ReviewListForm',
  data() {
    return {
      title: '',
      content: '',
      rank: ''
    }
  },
  computed: {
  ...mapGetters(['movie']),
  },
  methods: {
    ...mapActions(['createReview']),
    onSubmit() {
      this.createReview({
        moviePk: this.movie.pk, 
        title: this.title,
        content: this.content,
        rank: this.rank
        })
      this.content = ''
    }
  }
}
</script>

<style>
.star-rating {
  display: flex;
  flex-direction: row-reverse;
  font-size: 2.25rem;
  line-height: 2.5rem;
  justify-content: space-around;
  padding: 0 0.2em;
  text-align: center;
  width: 5em;
}
 
.star-rating input {
  display: none;
}
 
.star-rating label {
  -webkit-text-fill-color: transparent; /* Will override color (regardless of order) */
  -webkit-text-stroke-width: 2.3px;
  -webkit-text-stroke-color: #2b2a29;
  cursor: pointer;
}
 
.star-rating :checked ~ label {
  -webkit-text-fill-color: rgb(255, 0, 0);
}
 
.star-rating label:hover,
.star-rating label:hover ~ label {
  -webkit-text-fill-color: #ff0000;
}
</style>
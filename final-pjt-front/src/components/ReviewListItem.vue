<template>
  <div>
    <b-row class="d-flex justify-content-between pb-3">
      <b-col cols="9" >
          <div class="d-flex mb-2">
          <router-link 
          class="mt-1 font-weight-bold text-dark" 
          :to="{ name: 'profile', params: { username: review.user.username } }"
          style="font-size: 1.3rem">
            {{ review.user.username }}
          </router-link>
          <div class="heart-ratings ml-3">
            <div 
              class="heart-ratings-fill space-x-2 text-lg"
              :style="{ width: ratingToPercent + '%' }" 
            >
              <span>♥</span><span>♥</span><span>♥</span><span>♥</span><span>♥</span>
            </div>
            <div class="heart-ratings-base space-x-2 text-lg">
              <span>♥</span><span>♥</span><span>♥</span><span>♥</span><span>♥</span>
            </div>
          </div>
        </div>
        <p v-if="!isEditing">{{ payload.content }}</p>
        <p v-if="isEditing"><input type="text" v-model="payload.content"></p>
          <b-row v-if="isEditing">
            <b-button @click="onUpdate" variant="light" size="sm">Update</b-button>
            <b-button @click="switchIsEditing" size="sm">Cancel</b-button>
          </b-row>
      </b-col>
      <b-col cols="3" class="d-flex justify-content-end my-1">
        <b-container>
          <b-row class="d-flex justify-content-end">
            <small v-if="review.created_at === review.updated_at">{{ (review.created_at+'').substr(0,10) +' ' + (review.created_at+'').substr(11,8) }}</small>
            <small v-if="review.created_at !== review.updated_at">{{ '(수정됨) ' + (review.updated_at+'').substr(0,10) +' ' + (review.updated_at+'').substr(11,8) }} </small>
          </b-row>
          <b-row class="d-flex justify-content-end">
            <span v-if="currentUser.username === review.user.username && !isEditing" class="d-flex justify-content-end">
              <b-button @click="switchIsEditing" variant="light" size="sm">Edit</b-button> 
              <b-button @click="deleteReview(payload)" size="sm">Delete</b-button>
            </span>
          </b-row>

        </b-container>
      </b-col>
    </b-row>
    <hr>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ReviewListItem',
  props: { review: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        moviePk: '',
        reviewPk: this.review.pk,
        rank: this.review.pk,
        content: this.review.content
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser', 'movie']),
    ratingToPercent() {
      const score = +this.review.rank * 20;
      return score + 1.5;
    },
  },
  methods: {
    ...mapActions(['updateReview', 'deleteReview']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.payload.moviePk = this.movie.pk
      this.updateReview(this.payload)
      this.isEditing = false
    }
  },

}
</script>

<style>
.heart-ratings {
  font-size: 1.5rem;
  color: #aaa9a9; 
  position: relative;
  unicode-bidi: bidi-override;
  width: max-content;
  -webkit-text-fill-color: transparent; /* Will override color (regardless of order) */
  -webkit-text-stroke-width: 1px;
  -webkit-text-stroke-color: #959595;
}
 
.heart-ratings-fill {
  color: #fff58c;
  padding: 0;
  position: absolute;
  z-index: 1;
  display: flex;
  top: 0;
  left: 0;
  overflow: hidden;
  -webkit-text-fill-color: red;
}
 
.heart-ratings-base {
  z-index: 0;
  padding: 0;
}
</style>
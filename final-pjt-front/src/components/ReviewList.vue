<template>
  <b-container>
    <review-list-item 
      v-for="review in reviews" 
      :review="review" 
      :key="review.pk">
    </review-list-item>
    <review-list-form></review-list-form>
  </b-container>
</template>

<script>
import ReviewListItem from '@/components/ReviewListItem.vue'
import ReviewListForm from '@/components/ReviewListForm.vue'
// import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'ReviewList',
  components: { ReviewListForm, ReviewListItem },
  props: { reviews: Array },
}
</script>

<style>
/* .review-list {
  border: 1px solid blue;
} */
</style>
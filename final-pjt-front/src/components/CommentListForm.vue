<template>
  <form @submit.prevent="onSubmit" >
    <label class="mx-2" for="comment">comment: </label>
    <input type="text" id="comment" v-model="content" required>
    <button class="mx-2">Comment</button>
  </form>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListForm',
  data() {
    return {
      content: ''
    }
  },
  computed: {
    ...mapGetters(['article']),
  },
  methods: {
    ...mapActions(['createComment']),
    onSubmit() {
      this.createComment({ articlePk: this.article.pk, content: this.content, })
      this.content = ''
    }
  }
}
</script>

<style>

</style>
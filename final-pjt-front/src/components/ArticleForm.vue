<template>

  <form @submit.prevent="onSubmit" class="m-5">
    <input class="form-control form-control-lg mb-3" v-model="newArticle.title" type="text" id="title" placeholder="제목"/>
    <textarea class="form-control form-control-lg mb-3" v-model="newArticle.content" type="text" id="content" placeholder="내용" rows="5"></textarea>
    <button type="submit" class="btn-lg button-style">Create</button>
  </form>
</template>

<script>
import { mapActions } from 'vuex'

  export default {
    name: 'ArticleForm',
    props: {
      article: Object,
      action: String,
    },
    data() {
      return {
        newArticle: {
          title: this.article.title,
          content: this.article.content,
        }
      }
    },

    methods: {
      ...mapActions(['createArticle', 'updateArticle']),
      onSubmit() {
        if (this.action === 'create') {
          this.createArticle(this.newArticle)
        } else if (this.action === 'update') {
          const payload = {
            pk: this.article.pk,
            ...this.newArticle,
          }
          this.updateArticle(payload)
        }
      },
    },
  }
</script>

<style>
.button-style{
  border: 1px solid rgb(0, 0, 0);
  background: rgb(39, 247, 202);
}
</style>

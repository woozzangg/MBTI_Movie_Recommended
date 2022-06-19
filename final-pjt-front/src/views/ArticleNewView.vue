<template>
<b-container>

  <b-card>
    <b-card-body>
      <h1 class="m-5">New Article</h1>
      <article-form :article="article" action="create"></article-form>    
    </b-card-body>
  </b-card>
</b-container>
</template>

<script>
  import ArticleForm from '@/components/ArticleForm.vue'
  export default {
    name: 'AritcleNewView',
    components: { ArticleForm },
    data() {
      return {
        article: {
          pk: null,
          title: '',
          content: '',
        }
      }
    },
  }
</script>

<style>
.mint{
  background-color: #12d3a9;
}
.choco{
  background-color: #563d34;
}
</style>

<template>
  <b-container>
    <b-card>
      <b-card-body>
        <h1>자유게시판</h1>
        <ul class="d-flex flex-column align-items-center">
          <li class="w-100 mt-3 mb-2 d-flex justify-content-end">
            <b-button class="w-25 mr-3 text-decoration-none" v-if="isLoggedIn" :to="{ name: 'articleNew' }" block style="background-color: #12d3a9; color: #563d34; font-weight: bold;">글쓸래요</b-button>
          </li>
    
          <article-list-item v-for="article in articles"
          :key="article.id"
          :article="article">
          </article-list-item>
        </ul>
      </b-card-body>
    </b-card>
  </b-container>
</template>

<script>
import ArticleListItem from '@/components/ArticleListItem.vue'
  import { mapActions, mapGetters } from 'vuex'

  export default {
  components: { ArticleListItem },
    name: 'ArticleList',
    computed: {
      ...mapGetters(['articles', 'isLoggedIn'])
    },
    methods: {
      ...mapActions(['fetchArticles'])
    },
    created() {
      this.fetchArticles()
    },
  }
</script>

<style>
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
}
.choco{
  background-color: #563d34;
}
</style>

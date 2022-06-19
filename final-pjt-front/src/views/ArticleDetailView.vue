<template>
<b-container>
    <b-card class="row">
      <div class="d-flex justify-content-between">
        <router-link :to="{ name: 'profile', params: { username: article.user.username } }">
          <p class="font-weight-bold text-dark">
            {{ article.user.username }}
          </p>
        </router-link>
        <div>
          <p v-if="article.created_at === article.updated_at">{{ '작성시간 : ' + (article.created_at+'').substr(0,10) +' ' + (article.created_at+'').substr(11,8) }}</p>
          <p v-if="article.created_at !== article.updated_at">{{ '작성시간 : ' + (article.updated_at+'').substr(0,10) +' ' + (article.updated_at+'').substr(11,8) }} (수정됨)</p>
        </div>
      </div>
      <h2 class="font-weight-bold">
        {{article.title}}
        
      </h2>
      <b-card-text>
        {{article.content}}
      </b-card-text>
  
  
  <div class="d-flex justify-content-between">
        <b-button 
          @click="likeArticle(articlePk)"
          class="d-flex justify-content-between"
          style="background-color: #12d3a9; color: #563d34; font-weight: bold;"
        >
          <p class="p-0 m-0">좋아요</p>
          <p class="font-weight-bold px-1 py-0 m-0">{{ likeCount }}</p>
          <p class="p-0 m-0">개</p>
  
        </b-button> 
  
      <div v-if="isAuthor">
        <router-link :to="{ name: 'articleEdit', params: { articlePk } }">
          <b-button variant="light">Edit</b-button>
        </router-link>
        
        <b-button @click="deleteArticle(articlePk)">Delete</b-button>
        </div>
      </div>
      <hr>
    <comment-list :comments="article.comments"></comment-list>
    </b-card>
  </b-container>

</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import CommentList from '@/components/CommentList.vue'



  export default {
    name: 'ArticleDetail',
    components: { CommentList },
    data() {
      return {
        articlePk: this.$route.params.articlePk,
      }
    },
    computed: {
      ...mapGetters(['isAuthor', 'article']),
      likeCount() {
        return this.article.like_users?.length
      }
    },
    methods: {
      ...mapActions([
        'fetchArticle',
        'likeArticle',
        'deleteArticle',
      ])
    },
    created() {
      this.fetchArticle(this.articlePk)
    },
  }
</script>

<style>
.mint{
  background-color: #12d3a9;
}
.choco{
  background-color: #1d2726;
}
</style>

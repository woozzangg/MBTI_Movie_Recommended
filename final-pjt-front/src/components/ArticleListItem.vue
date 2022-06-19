<template>
    <b-container>
      <router-link 
          :to="{ name: 'article', params: {articlePk: article.pk} }"
          class="text-decoration-none text-reset">
        
        <b-card 
        :title=article.title
        tag="article"
        
        class="mb-2" 
        >
          <b-card-body>
            <b-card-text class="multiLine">
            {{ article.content }}
            </b-card-text>
              <span class="d-flex justify-content-end">
              붐업!! {{ article.like_count }} | 댓글 {{article.comment_count}}
              </span>
          </b-card-body>
          <b-card-footer class="d-flex justify-content-between">
            <div>
              <span v-if="article.created_at === article.updated_at">{{ '작성시간 : ' + (article.created_at+'').substr(0,10) +' ' + (article.created_at+'').substr(11,8) }}</span>
              <span v-if="article.created_at !== article.updated_at">{{ '작성시간 : ' + (article.updated_at+'').substr(0,10) +' ' + (article.updated_at+'').substr(11,8) }} (수정됨)</span>
            </div>
            <div>
              <router-link :to="{ name: 'profile', params: { username } }">
              <strong class="text-dark">{{ article.user.username }}</strong>
                  
              </router-link>
            </div>
          </b-card-footer>

        </b-card>
      </router-link>
    </b-container>
</template>

<script>
export default {
  name: 'ArticleListItem',
  props: {
    article: Object,
  },
    computed: {
    username() {
      return this.article.user.username
    },
  },
}
</script>

<style>
.multiLine{
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
}

</style>
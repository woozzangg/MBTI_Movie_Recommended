<template>
  <b-container>
    <b-card>
      <h2><strong>{{ profile.username }}</strong>님의 프로필 </h2>
      <!-- <b-button size="sm" @click="follow(profile.username)">Follow</b-button> -->
      <h5>팔로워 : {{ followersCount }} / 팔로잉 : {{ followingsCount }}</h5>
      <div v-if="profile.username!=currentUser.username">
        <b-button v-if="followersCount" @click="follow(profile.username)" class="btn btn-secondary "> UnFollow </b-button>
        <b-button v-else @click="follow(profile.username)" class="btn btn-primary ">Follow </b-button>
        <p v-if="followersCount" class="st-font">{{ profile.username }}님을 팔로우 중 입니다.</p>
      </div>
      
      <!-- MBTI 내용 들어갈것 -->
      <div>
        <b-card no-body>
          <b-tabs v-model="tabIndex" card content-class="my-3" active-nav-item-class="font-weight-bold text-danger" >
            <b-tab title="좋아요한 영화" active>
              <b-card-group class="row" id="my-table">
                <movie-list-item v-for="movie in profile.liked_movies"
                :key="movie.id"
                :movie="movie">
                </movie-list-item>
              </b-card-group>
            </b-tab>
            <b-tab title="좋아요한 게시글">
                <profile-article-list-item v-for="article in profile.like_articles"
                :key="article.id"
                :article="article">
                </profile-article-list-item>
            </b-tab>
            <b-tab title="작성한 게시글">
                <profile-article-list-item v-for="article in profile.articles"
                :key="article.id"
                :article="article">
                </profile-article-list-item>
            </b-tab>
            <b-tab title="작성한 댓글">
              <b-card-text>
                <comment-list-item 
                  v-for="comment in profile.comments" 
                  :comment="comment" 
                  :key="comment.pk">
                </comment-list-item>
              </b-card-text>
            </b-tab>
          </b-tabs>
        </b-card>
      </div>
      <!-- <div class=" my-5" >
        <div class="w-100 btn-group btn-group-sm overflow-auto" role="group">
          <b-button id="btn-0" class="btn my-2 my-sm-2" pill variant="outline-secondary"
          
            >좋아요한 영화</b-button>
          <b-button id="btn-1" class="btn my-2 my-sm-2" pill variant="outline-secondary"
          
            >작성한 게시글</b-button>
          <b-button id="btn-2" class="btn my-2 my-sm-2" pill variant="outline-secondary"
          
            >작성한 댓글</b-button>
          <b-button id="btn-3" class="btn my-2 my-sm-2" pill variant="outline-secondary"
          
            >작성한 리뷰</b-button>
        </div>
      </div> -->


      <!-- <div class="article-list">
        <h2>작성한 게시글</h2>
        <ul>
          <li v-for="article in profile.articles" :key="article.pk">
            <router-link :to="{ name: 'article', params: { articlePk: article.pk } }">
              {{ article.title }}
            </router-link>
          </li>
        </ul>
      </div>
      <div class="like-list">
        <h2>좋아요 한 글</h2>
        <ul>
          <li v-for="article in profile.like_articles" :key="article.pk">
            <router-link :to="{ name: 'article', params: { articlePk: article.pk } }">
              {{ article.title }}
            </router-link>
          </li>
        </ul>
      </div> -->
    </b-card>
  </b-container>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import MovieListItem from '@/components/MovieListItem.vue'
import ProfileArticleListItem from '@/components/ProfileArticleListItem.vue'
import CommentListItem from '@/components/CommentListItem.vue'


export default {
  data() {
    return {
      tabIndex: 1
    }
  },
  components: { MovieListItem, ProfileArticleListItem, CommentListItem },
  name: 'ProfileView',
  computed: {
    ...mapGetters(['profile', 'currentUser']),
    followersCount() {
      return this.profile.followers?.length
    },
    followingsCount() {
      return this.profile.followings?.length
    },
  },
  methods: {
    ...mapActions(['fetchProfile', 'follow'])
  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
  },
}
</script>
<style>
.article-list {
  border: 1px solid black;
  margin: 2rem;
  padding: 2rem;
}
.like-list {
  border: 1px solid rgb(10, 4, 4);
  margin: 2rem;
  padding: 2rem;
}
.nav-link {
  color: black;
}
</style>

<template>
  <b-container>
    <b-card>
      <template #header>
        <b-row class="pt-3"
        :style="{'background-image': 'linear-gradient(rgba(0, 0, 0, 0.9), rgba(0, 0, 0, 0.6)), url(' + `https://image.tmdb.org/t/p/original/${movie.backdrop_path}` + ')',
                  'background-size': 'cover'}">
          <b-col sm="12" lg="4" class="mb-5">
            <a v-b-modal.image-modal>
              <img :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`" alt="poster_image" class="w-100">
              <b-modal id="image-modal" size="xl" title="이게 모달?" hide-footer>
                <img :src="`https://image.tmdb.org/t/p/original/${movie.backdrop_path}`" alt="backdrop_img" class="w-100">
                <div class="video-container my-1" v-for="video in movie.videos"
                  :key="video.id"
                  :video="video">
                    <iframe :src="`https://www.youtube.com/embed/${video.video_path}`" frameborder="0"></iframe>
                </div>
              </b-modal>
            </a>
          </b-col>
          <b-col class="mx-5 text-white d-flex flex-column">
            <div class="mb-5">
              <b-card-title class="font-weight-bold mb-0">{{ movie.title }}</b-card-title>
              <small class="mt-0 pt-0">{{ getGenreNames() }}</small>
              <b-card-sub-title class="mt-2 font-weight-bold "><em>{{ movie.tagline }}</em></b-card-sub-title>
              <div class="star-ratings">
                <div 
                  class="star-ratings-fill space-x-2 text-lg"
                  :style="{ width: ratingToPercent + '%' }"
                >
                  <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
                </div>
                <div class="star-ratings-base space-x-2 text-lg">
                  <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
                </div>
              </div>
              <b-card-text class="line10">{{ movie.overview }}</b-card-text>
            </div>
            <ul class="d-flex">
              <movie-provider-item 
              v-for="path in movie.paths"
              :key="path.id"
              :path="path">
              </movie-provider-item>
            </ul>
            <div class="d-flex justify-content-end mt-5">
              <b-button class="d-flex"
                @click="likeMovie(moviePk)"
                style="background-color: #12d3a9; color: #563d34; font-weight: bold;"
              >
                <p class="p-0 m-0">좋아요</p>
                <p class="font-weight-bold px-1 py-0 m-0">{{ likeCount }}</p>
                <p class="p-0 m-0">개</p>
              </b-button>
            </div>
          </b-col>
        </b-row>
      </template>
      <review-list :reviews="movie.reviews"></review-list>
    </b-card>
  </b-container>

</template>

<script>
  import MovieProviderItem from '@/components/MovieProviderItem.vue'
  import ReviewList from '@/components/ReviewList.vue'
  import { mapGetters, mapActions } from 'vuex'

  export default {
    components: { MovieProviderItem, ReviewList },
    name: 'MovieDetail',
    data() {
      return {
        moviePk: this.$route.params.moviePk,
      }
    },
    computed: {
      ...mapGetters(['movie']),
      likeCount() {
        return this.movie.like_users?.length
      },
      ratingToPercent() {
        const score = +this.movie.vote_average * 10;
        return score + 1.5;
      },
    },
    methods: {
      ...mapActions([
        'fetchMovie',
        'likeMovie',
      ]),
      getGenreNames() {
        var elems = this.movie.genres
        var values = [].map.call(elems, function(obj) {
          return ' ' + obj.name;
        });
        return values.toString()
      }
    },
    created() {
      this.fetchMovie(this.moviePk)
    },
  }
</script>

<style>
.line10{
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 10;
  -webkit-box-orient: vertical;
}

.video-container {
  position: relative;
  padding-top: 56.28%;
}

.video-container > iframe {
  position: absolute;
  top: 0;
  bottom: 0;
  width: 100%;
  height: 100%;
}

.star-ratings {
  font-size: 1.5rem;
  color: #aaa9a9; 
  position: relative;
  unicode-bidi: bidi-override;
  width: max-content;
  -webkit-text-fill-color: transparent; /* Will override color (regardless of order) */
  -webkit-text-stroke-width: 1px;
  -webkit-text-stroke-color: #959595;
}
 
.star-ratings-fill {
  color: #fff58c;
  padding: 0;
  position: absolute;
  z-index: 1;
  display: flex;
  top: 0;
  left: 0;
  overflow: hidden;
  -webkit-text-fill-color: gold;
}
 
.star-ratings-base {
  z-index: 0;
  padding: 0;
}

</style>
<template>
  <b-container>
        <b-card>
            <b-card-group class="row" id="my-page3">
                <movie-list-item v-for="movie in movies.slice((currentPage-1)*perPage, currentPage*perPage)"
                :key="movie.id"
                :movie="movie">
                </movie-list-item>
              </b-card-group>
              <a class="d-flex justify-content-center" @click="scrollToTop()">
                <b-pagination
                  class="bg-white"
                  pills size="lg"
                  v-model="currentPage"
                  :total-rows="rows"
                  :per-page="perPage"
                  aria-controls="my-page3"
                ></b-pagination>
              </a>
        </b-card>
  </b-container>
</template>

<script>
  import MovieListItem from '@/components/MovieListItem.vue'
  import { mapActions, mapGetters } from 'vuex'

  export default {
    data() {
      return {
        perPage: 20,
        currentPage: 1,
      }
    },
    components: { MovieListItem },
    name: 'MovieSearchList',
    computed: {
      ...mapGetters(['movies', 'rows']),
    },
    methods: {
      ...mapActions(['fetchSearchMovies']),
      scrollToTop() {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }
    },
    created() {
      const payload = this.$route.params.word
      this.fetchSearchMovies(payload)
    },
  }
</script>

<style>

</style>
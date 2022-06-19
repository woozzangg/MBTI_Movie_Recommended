<template>
  <b-container>
        <b-card no-body>
          <b-tabs card content-class="my-3" active-nav-item-class="font-weight-bold text-danger" >
            <b-tab @click="fetchMovies()" title="인기 영화" active>
              <b-card-group class="row" id="my-page1">
                <movie-list-item v-for="movie in movies.slice((currentPage-1)*perPage, currentPage*perPage)"
                :key="movie.id"
                :movie="movie">
                </movie-list-item>
              </b-card-group>
              <a class="d-flex justify-content-center" @click="scrollToTop()">
                <b-pagination
                  class="bg-white "
                  pills size="lg"
                  v-model="currentPage"
                  :total-rows="rows"
                  :per-page="perPage"
                  aria-controls="my-page1"
                ></b-pagination>
              </a>
            </b-tab>
            <b-tab @click="fetchMoviesRMBTI()" v-if="isLoggedIn" title="MBTI 추천영화">
              <b-card-group class="row" id="my-page2">
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
                  aria-controls="my-page2"
                ></b-pagination>
              </a>
            </b-tab>
            <b-tab @click="fetchMoviesProvider(providerPk)" v-if="isLoggedIn" title="OTT로 검색">
              <div class="m-2">
                <b-form inline>
                  <label class="mr-sm-2" for="inline-form-custom-select-pref">Provider</label>
                  <b-form-select
                    id="inline-form-custom-select-pref"
                    class="mb-2 mr-sm-2 mb-sm-0"
                    :options="[
                    { text: 'NetFlix', value: 8 }, 
                    { text: 'NaverStore', value: 96 }, 
                    { text: 'WatCha', value: 97 }, 
                    { text: 'AmazonPrimeVideo', value: 119 },
                    { text: 'DisneyPlus', value: 337 },
                    { text: 'AppleTVPlus', value: 350 },
                    { text: 'Wavve', value: 356 },
                    ]"
                    v-model="providerPk"
                  ></b-form-select>
                  <b-button @click="fetchMoviesProvider(providerPk)">SEARCH</b-button>
                </b-form>
              </div>
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
            </b-tab>
            <b-tab @click="fetchMoviesRProvider({provider1Pk, provider2Pk})" v-if="isLoggedIn" title="OTT 비교 검색">
              <div class="m-2">
                <b-form inline>
                  <b-form-select
                    id="inline-form-custom-select-pref"
                    class="mb-2 mr-sm-2 mb-sm-0"
                    :options="[
                    { text: 'NetFlix', value: 8 }, 
                    { text: 'NaverStore', value: 96 }, 
                    { text: 'WatCha', value: 97 }, 
                    { text: 'AmazonPrimeVideo', value: 119 },
                    { text: 'DisneyPlus', value: 337 },
                    { text: 'AppleTVPlus', value: 350 },
                    { text: 'Wavve', value: 356 },
                    ]"
                    v-model="provider1Pk"
                  ></b-form-select>
                  <label class="mr-sm-2" for="inline-form-custom-select-pref">있</label>
                  <b-form-select
                    id="inline-form-custom-select-pref"
                    class="mb-2 mr-sm-2 mb-sm-0"
                    :options="[
                    { text: 'WatCha', value: 97 }, 
                    { text: 'NetFlix', value: 8 }, 
                    { text: 'NaverStore', value: 96 }, 
                    { text: 'AmazonPrimeVideo', value: 119 },
                    { text: 'DisneyPlus', value: 337 },
                    { text: 'AppleTVPlus', value: 350 },
                    { text: 'Wavve', value: 356 },
                    ]"
                    v-model="provider2Pk"
                  ></b-form-select>
                  <label class="mr-sm-2" for="inline-form-custom-select-pref">없</label>
                  <b-button @click="fetchMoviesRProvider({provider1Pk, provider2Pk})">SEARCH</b-button>
                </b-form>
              </div>
              <b-card-group class="row" id="my-page4">
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
                  aria-controls="my-page4"
                ></b-pagination>
              </a>
            </b-tab>
          </b-tabs>
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
        providerPk: 8,
        provider1Pk: 8,
        provider2Pk: 97,
      }
    },
    components: { MovieListItem },
    name: 'MovieList',
    computed: {
      ...mapGetters(['movies', 'rows']),
    },
    methods: {
      ...mapActions(['fetchMovies', 'fetchMoviesRMBTI', 'fetchMoviesRProvider', 'fetchMoviesProvider', 'fetchMoviesGenre', 'isLoggedIn']),
      scrollToTop() {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }
    },
    created() {
      this.fetchMovies()
    },
  }
</script>

<style>

</style>
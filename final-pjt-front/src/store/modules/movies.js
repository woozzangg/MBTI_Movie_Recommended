import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

export default {
    state: {
      movies: [],
      movie: {},
      images: {},
    },
  
    getters: {
      movies: state => state.movies,
      rows: state => state.movies.length,
      movie: state => state.movie,
      images: state => state.image,
    },
  
    mutations: {
      SET_MOVIES: (state, movies) => state.movies = movies,
      SET_MOVIE: (state, movie) => state.movie = movie,
      SET_MOVIE_REVIEWS: (state, reviews) => (state.movie.reviews = reviews),
    },
  
    actions: {
      fetchMovies({ commit }) {
        axios({
          url: drf.movies.movies(),
          method: 'get',
        })
          .then(res => commit('SET_MOVIES', res.data))
          .catch(err => console.error(err.response))
      },
      fetchMoviesRMBTI({ commit, getters }) {
        axios({
          url: drf.movies.moviesRecommendedMBTI(),
          method: 'get',
          headers: getters.authHeader,
        })
          .then(res => commit('SET_MOVIES', res.data))
          .catch(err => console.error(err.response))
      },
      fetchMoviesRProvider({ commit }, {provider1Pk, provider2Pk}) {
        console.log(provider1Pk, provider2Pk)
        axios({
          url: drf.movies.moviesRecommendedProvider(provider1Pk, provider2Pk),
          method: 'get',
        })
          .then(res => commit('SET_MOVIES', res.data))
          .catch(err => console.error(err.response))
      },
      fetchMoviesProvider({ commit }, providerPk) {
        axios({
          url: drf.movies.moviesProvider(providerPk),
          method: 'get',
        })
          .then(res => commit('SET_MOVIES', res.data))
          .catch(err => console.error(err.response))
      },
      fetchMoviesGenre({ commit }, genrePk) {
        axios({
          url: drf.movies.moviesGenre(genrePk),
          method: 'get',
        })
          .then(res => commit('SET_MOVIES', res.data))
          .catch(err => console.error(err.response))
      },
      fetchSearchMovies({ commit }, word) {
        console.log(word)
        axios({
          url: drf.movies.moviesSearch(word),
          method: 'get',
        })
          .then(res => commit('SET_MOVIES', res.data))
          .catch(err => console.error(err.response))
      },
      fetchMovie({ commit }, moviePk) {
        axios({
          url: drf.movies.movie(moviePk),
          method: 'get',
        })
          .then(res => commit('SET_MOVIE', res.data))
          .catch(err => {
            console.error(err.response)
            if (err.response.status === 404) {
              router.push({ name: 'NotFound404' })
            }
          })
      },
  
      likeMovie({ commit, getters }, moviePk) {
        axios({
          url: drf.movies.likeMovie(moviePk),
          method: 'post',
          headers: getters.authHeader,
        })
          .then(res => commit('SET_MOVIE', res.data))
          .catch(err => console.error(err.response))
      },
  
      createReview({ commit, getters }, { rank, moviePk, content }) {
        const review = { rank, content }
  
        axios({
          url: drf.movies.reviews(moviePk),
          method: 'post',
          data: review,
          headers: getters.authHeader,
        })
          .then(res => {
            commit('SET_MOVIE_REVIEWS', res.data)
          })
          .catch(err => console.error(err.response))
      },
  
      updateReview({ commit, getters }, { moviePk, reviewPk, content }) {
        const review = { content }
  
        axios({
          url: drf.movies.review(moviePk, reviewPk),
          method: 'put',
          data: review,
          headers: getters.authHeader,
        })
          .then(res => {
            commit('SET_MOVIE_REVIEWS', res.data)
          })
          .catch(err => console.error(err.response))
      },
  
      deleteComment({ commit, getters }, { moviePk, reviewPk }) {
          if (confirm('정말 삭제하시겠습니까?')) {
            axios({
              url: drf.movies.review(moviePk, reviewPk),
              method: 'delete',
              data: {},
              headers: getters.authHeader,
            })
              .then(res => {
                commit('SET_MOVIE_REVIEWS', res.data)
              })
              .catch(err => console.error(err.response))
          }
        },
    },
  }
  
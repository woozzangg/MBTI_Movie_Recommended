<template>
  <b-col md="4" lg="3" class="mb-3 movie-item">
    <router-link 
    :to="{ name: 'movie', params: {moviePk: movie.pk} }"
    class="text-decoration-none text-reset"
    >
      <div v-b-hover="handleHover" class="h-100">
        <b-card v-if="isHovered"
        :title="movie.title"
        :img-src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`"
        img-alt="Poster" overlay
        class="movie-hover font-weight-bold">
          <b-card-text>{{ movie.overview }}</b-card-text>
        </b-card>
        <b-card v-else
        :title="movie.title"
        :img-src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`"
        img-alt="Poster" img-top
        class="h-100">
        </b-card>
      </div>
    </router-link>
  </b-col>
</template>

<script>
export default {
  name: 'MovieListItem',
  props: {
    movie: Object,
  },
  data() {
    return {
      isHovered: false
    }
  },
  methods: {
    handleHover(hovered) {
      this.isHovered = hovered
    }
  }
}
</script>

<style>
.movie-hover img{
  opacity: 0.4;
}
.movie-hover .card-text{
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 5;
  -webkit-box-orient: vertical;
}
.movie-hover .card-title{
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
}
</style>
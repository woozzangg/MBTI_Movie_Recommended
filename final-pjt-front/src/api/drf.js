const HOST = 'http://localhost:8000/api/v1/'

const ACCOUNTS = 'accounts/'
const COMMUNITY = 'community/'
const COMMENTS = 'comments/'
const MOVIES = 'movies/'
const REVIEW = 'review/'

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    // Token 으로 현재 user 판단
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    // username으로 프로필 제공
    profile: username => HOST + ACCOUNTS + 'profile/' + username,
    follow: username => HOST + ACCOUNTS + 'profile/' + username + '/follow/'
  },
  community: {
    articles: () => HOST + COMMUNITY,
    article: articlePk => HOST + COMMUNITY + `${articlePk}/`,
    likeArticle: articlePk => HOST + COMMUNITY + `${articlePk}/` + 'like/',
    comments: articlePk => HOST + COMMUNITY + `${articlePk}/` + COMMENTS,
    comment: (articlePk, commentPk) =>
      HOST + COMMUNITY + `${articlePk}/` + COMMENTS + `${commentPk}/`,
  },
  movies: {
    movies: () => HOST + MOVIES,
    moviesGenre: genrePk => HOST + MOVIES + `${genrePk}/`,
    moviesSearch: word => HOST + MOVIES + `search/${word}/`,
    moviesProvider: providerPk => HOST + MOVIES + 'provider/' +`${providerPk}`,
    moviesRecommendedMBTI: () => HOST + MOVIES + 'recommended/mbti/',
    moviesRecommendedProvider: (provider1Pk, provider2Pk) => HOST + MOVIES + 'provider/' + `${provider1Pk}/` + 'not/' + `${provider2Pk}/`,
    movie: moviePk => HOST + MOVIES + `${moviePk}/`,
    likeMovie: moviePk => HOST + MOVIES + `${moviePk}/` + 'like/',
    reviews: moviePk => HOST + MOVIES + `${moviePk}/` + REVIEW,
    review: (moviePk, reviewPk) => HOST + MOVIES + `${moviePk}/` + REVIEW + `${reviewPk}/`,
    reviewLike: (moviePk, reviewPk) => HOST + MOVIES + `${moviePk}/` + REVIEW + `${reviewPk}/` + 'like/',
  },
}

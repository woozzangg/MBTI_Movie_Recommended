from turtle import back
import requests
import os
from bs4 import BeautifulSoup
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MBTI.settings")

import django
django.setup()

from movies.models import Movie, Genre, Provider, Path, Video

API_KEY = "a2d4a7ce34088010ccefc95694bb0f14"
BASE_URL = 'https://api.themoviedb.org/3/movie'


def get_genre_data():
    genre_dict = {
        28: '액션',
        12: '모험',
        16: '애니메이션',
        35: '코미디',
        80: '범죄',
        99: '다큐멘터리',
        18: '드라마',
        10751: '가족',
        14: '판타지',
        36: '역사',
        27: '공포',
        10402: '음악',
        9648: '미스테리',
        10749: '로맨스',
        878: 'SF',
        10770: 'TV 영화',
        53: '스릴러',
        10752: '전쟁',
        37: '서부'
    }
    return genre_dict


def get_provider_data():
    provider_dict = {
        356: 'wavve', 
        337: 'Disney Plus', 
        8: 'Netflix', 
        96: 'Naver Store', 
        119: 'Amazon Prime Video', 
        97: 'Watcha', 
        350: 'Apple TV Plus'
        }
    return provider_dict


def parse_provider_data(movie_id):
    result = {'providers': set(), 'provider_link': ''}
    PROVIDER_URL = f"/{movie_id}/watch/providers"
    params = {
        'api_key': API_KEY,
        'language': 'ko-KR',
    }
    api_result = requests.get(BASE_URL + PROVIDER_URL, params=params).json().get('results').get('KR')
    if api_result:
        if api_result.get('buy'):
            for provider in api_result.get('buy'):
                result['providers'].add(provider.get('provider_id'))
        if api_result.get('rent'):
            for provider in api_result.get('rent'):
                result['providers'].add(provider.get('provider_id'))
        if api_result.get('flatrate'):
            for provider in api_result.get('flatrate'):
                result['providers'].add(provider.get('provider_id'))
        
        result['provider_link'] = api_result.get('link')
        result['providers'] = list(result['providers'])
        
    return result


def get_provider_url(link):
    response = requests.get(link, headers={'User-Agent': 'Chrome'})
    result = {}

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        title = soup.find(class_="right_column")
        for link in title.find_all(rel="noopener", target="_blank"):
            if link.get('title'):
                for provider in Provider.objects.all().values():
                    if provider['name'] in link['title']:
                        if 'Buy' in link['title']:
                            result[provider['name']] = link['href']
                        if 'Rent' in link['title']:
                            result[provider['name']] = link['href']
                        if 'Watch' in link['title']:
                            result[provider['name']] = link['href']
        return result
    else:
        print(response.status_code)


def parse_movie_data():
    POPULAR_URL = "/popular"
    result = {
        'movies': [],
        }
    for page in range(1, 4):
        print(page)
        params = {
            'api_key': API_KEY,
            'language': 'ko-KR',
            'page': page
        }

        result['movies'].extend(requests.get(BASE_URL + POPULAR_URL, params=params).json().get('results'))

    return result


def parse_detail_data(movie_id):
    DETAIL_URL = f"/{movie_id}"

    params = {
    'api_key': API_KEY,
    'language': 'ko-KR',
    }
    result = requests.get(BASE_URL + DETAIL_URL, params=params).json()

    return result


def parse_video_data(movie_id):
    VIDEO_URL = f"/{movie_id}/videos"
    result = []

    params = {
    'api_key': API_KEY,
    'language': 'ko-KR',
    }

    result.extend(requests.get(BASE_URL + VIDEO_URL, params=params).json().get('results'))

    return result


if __name__ == '__main__':
    movies = parse_movie_data().get('movies')
    genres = get_genre_data()
    providers = get_provider_data()

    for genre_id, name in genres.items():
        Genre(id=genre_id, name=name).save()

    for provider_id, provider_name in providers.items():
        Provider(id=provider_id, name=provider_name).save()

    for movie in movies:
        movie_id = movie.get('id')
        title = movie.get('title')
        overview = movie.get('overview')
        release_date = movie.get('release_date')
        vote_average = movie.get('vote_average')
        vote_count = movie.get('vote_count')
        popularity = movie.get('popularity')
        poster_path = movie.get('poster_path')
        movie_genres = movie.get('genre_ids')

        if id and title and overview and poster_path:
            detail_data = parse_detail_data(movie_id)

            backdrop_path = detail_data.get('backdrop_path')
            tagline = detail_data.get('tagline')
            saved_movie = Movie(
                id=movie_id, 
                title=title, 
                overview=overview, 
                release_date=release_date, 
                vote_average=vote_average,
                vote_count=vote_count,
                popularity=popularity,
                poster_path=poster_path,
                backdrop_path=backdrop_path,
                tagline=tagline
                )
            saved_movie.save()

            for genre_id in movie_genres:
                saved_movie.genres.add(genre_id)

            videos = parse_video_data(movie_id)
            for video in videos:
                if video.get('site') == 'YouTube':
                    if video.get('key'):
                        Video(video_path=video.get('key'), movie=saved_movie).save()

            provider_dict = parse_provider_data(movie_id)

            if provider_dict.get('provider_link'):
                for provider_name, provider_link in get_provider_url(provider_dict.get('provider_link')).items():
                    if provider_link:
                        provider = Provider.objects.get(name=provider_name)
                        saved_movie.providers.add(provider)
                        Path(provider_path=provider_link, movie=saved_movie, provider=provider).save()

        else:
            print(movie_id, title)

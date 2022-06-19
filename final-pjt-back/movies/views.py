from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_safe
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q

from .models import Movie, Review, Genre, Provider
from .serializers import (
    MovieListSerializer,
    MovieSerializer,
    ReviewSerializer
    )


@api_view(['GET'])
def movie_index(request):
    movies = Movie.objects.all().order_by('-popularity')
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_index_genre(request, genre_pk):
    genre = get_object_or_404(Genre, pk=genre_pk)
    movies = Movie.objects.filter(genres=genre).order_by('-popularity')
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_index_provider(request, provider_pk):
    provider = get_object_or_404(Provider, pk=provider_pk)
    movies = Movie.objects.filter(providers=provider).order_by('-popularity')
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_search(request, word):
    movies = Movie.objects.filter(title__contains=word).order_by('-popularity')
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_recommended_mbti(request):
    user = request.user
    if user.ie:
        movies_ie = Movie.objects.filter(I_score__gt=0).order_by('-like_users')
    else:
        movies_ie = Movie.objects.filter(E_score__gt=0).order_by('-like_users')
    if user.ns:
        movies_ns = Movie.objects.filter(N_score__gt=0).order_by('-like_users')
    else:
        movies_ns = Movie.objects.filter(N_score__gt=0).order_by('-like_users')
    if user.ft:
        movies_ft = Movie.objects.filter(F_score__gt=0).order_by('-like_users')
    else:
        movies_ft = Movie.objects.filter(F_score__gt=0).order_by('-like_users')
    if user.pj:
        movies_pj = Movie.objects.filter(P_score__gt=0).order_by('-like_users')
    else:
        movies_pj = Movie.objects.filter(P_score__gt=0).order_by('-like_users')

    movies = movies_ie | movies_ft | movies_ns | movies_pj
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_recommended_provider(request, provider1_pk, provider2_pk):
    provider1 = get_object_or_404(Provider, pk=provider1_pk)
    provider2 = get_object_or_404(Provider, pk=provider2_pk)
    movies = Movie.objects.filter(providers=provider1).filter(~Q(providers=provider2)).order_by('-popularity')
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['POST'])
def movie_like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if movie.like_users.filter(pk=user.pk).exists():
        if user.ie:
            movie.I_score -= 1
        else:
            movie.E_score -= 1
        if user.ns:
            movie.N_score -= 1
        else:
            movie.S_score -= 1
        if user.ft:
            movie.F_score -= 1
        else:
            movie.T_score -= 1
        if user.pj:
            movie.P_score -= 1
        else:
            movie.J_score -= 1
        movie.save()
        movie.like_users.remove(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    else:
        if user.ie:
            movie.I_score += 1
        else:
            movie.E_score += 1
        if user.ns:
            movie.N_score += 1
        else:
            movie.S_score += 1
        if user.ft:
            movie.F_score += 1
        else:
            movie.T_score += 1
        if user.pj:
            movie.P_score += 1
        else:
            movie.J_score += 1
        movie.save()
        movie.like_users.add(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


@api_view(['POST'])
def review_create(request, movie_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    
    serializer = ReviewSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=user)

        reviews = movie.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def review_update_delete(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)

    def update_review():
        if request.user == review.user:
            serializer = ReviewSerializer(instance=review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                reviews = movie.reviews.all()
                serializer = ReviewSerializer(reviews, many=True)
                return Response(serializer.data)

    def delete_review():
        if request.user == review.user:
            review.delete()
            reviews = movie.reviews.all()
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data)
    
    if request.method == 'PUT':
        return update_review()
    elif request.method == 'DELETE':
        return delete_review()


@api_view(['POST'])
def review_like(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)
    user = request.user

    if review.like_users.filter(pk=user.pk).exists():
        review.like_users.remove(user)
        reviews = movie.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    else:
        review.like_users.add(user)
        reviews = movie.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

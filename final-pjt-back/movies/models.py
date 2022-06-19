from django.db import models
from django.conf import settings


class Genre(models.Model):
    name = models.CharField(max_length=50)


class Provider(models.Model):
    name = models.CharField(max_length=50)


class Movie(models.Model):
    genres = models.ManyToManyField(Genre, related_name='movies')
    providers = models.ManyToManyField(Provider, related_name='movies')
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    popularity = models.FloatField()
    poster_path = models.CharField(max_length=200)
    backdrop_path = models.CharField(max_length=200)
    tagline = models.TextField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_movies', blank=True)
    I_score = models.IntegerField(default=0)
    E_score = models.IntegerField(default=0)
    N_score = models.IntegerField(default=0)
    S_score = models.IntegerField(default=0)
    F_score = models.IntegerField(default=0)
    T_score = models.IntegerField(default=0)
    J_score = models.IntegerField(default=0)
    P_score = models.IntegerField(default=0)


class Review(models.Model):
    rank = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews', blank=True)


class Path(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='paths')
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    provider_path = models.URLField()


class Video(models.Model):
    video_path = models.CharField(max_length=200)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='videos')
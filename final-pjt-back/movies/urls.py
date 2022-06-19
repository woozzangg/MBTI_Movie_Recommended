from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_index),
    path('search/<word>/', views.movie_search),
    path('genre/<int:genre_pk>/', views.movie_index_genre),
    path('provider/<int:provider_pk>/', views.movie_index_provider),
    path('recommended/mbti/', views.movie_recommended_mbti),
    path('provider/<int:provider1_pk>/not/<int:provider2_pk>/', views.movie_recommended_provider),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/like/', views.movie_like),
    path('<int:movie_pk>/review/', views.review_create),
    path('<int:movie_pk>/review/<int:review_pk>', views.review_update_delete),
    path('<int:movie_pk>/review/<int:review_pk>/like/', views.review_like),
]
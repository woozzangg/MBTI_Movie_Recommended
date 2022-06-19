from rest_framework import serializers
from django.contrib.auth import get_user_model
from community.models import Article, Comment
from movies.models import Movie

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class ProfileSerializer(serializers.ModelSerializer):
    
    class ArticleSerializer(serializers.ModelSerializer):
        user = UserSerializer(read_only=True)

        class Meta:
            model = Article
            fields = ('pk', 'user', 'title', 'content', 'created_at', 'updated_at')

    class MovieListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('pk', 'title', 'overview', 'poster_path',)
    
    class CommentSerializer(serializers.ModelSerializer):   
        user = UserSerializer(read_only=True)
        class Meta:
            model = Comment
            fields = ('pk', 'user', 'content', 'article', 'created_at', 'updated_at')
            read_only_fields = ('article', )

    articles = ArticleSerializer(many=True)
    comments = CommentSerializer(many=True)
    liked_movies = MovieListSerializer(many=True)
    like_articles = ArticleSerializer(many=True)
    articles = ArticleSerializer(many=True)
    followers = UserSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'email', 'like_articles', 'liked_movies', 'articles', 'followings', 'followers', 'articles', 'comments')


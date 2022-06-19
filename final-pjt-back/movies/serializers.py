from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Movie, Review, Path, Genre, Video

User = get_user_model()

class ReviewSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)
    like_users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Review
        fields = ('id', 'content', 'rank', 'user', 'like_users', 'created_at', 'updated_at')
        read_only_fields = ('like_users', )


class MovieSerializer(serializers.ModelSerializer):
    class VideoSerializer(serializers.ModelSerializer):
        class Meta:
            model = Video
            fields = ('video_path', )

    class PathSerializer(serializers.ModelSerializer):
        class Meta:
            model = Path
            fields = ('provider_path', 'provider_id')

    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('name', )
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    videos = VideoSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    paths = PathSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    like_users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = ('pk', "reviews", "paths", "genres", "like_users", "title", "overview", "release_date", "vote_average", "vote_count", "poster_path", "backdrop_path", "tagline", "videos")
        

class MovieListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('pk', 'title', 'overview', 'poster_path',)
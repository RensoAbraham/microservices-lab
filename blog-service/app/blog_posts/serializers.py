from rest_framework import serializers
from .models import Post
from blog_authors.serializers import AuthorSerializer
from blog_categories.serializers import CategorySerializer

class PostListSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    excerpt = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'excerpt', 'author', 'category', 'published_at']

    def get_excerpt(self, obj):
        # Devuelve los primeros 150 caracteres del cuerpo del post
        return obj.body[:150] + '...' if len(obj.body) > 150 else obj.body


class PostDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'body', 'author', 'category', 'published_at', 'views']
from rest_framework import serializers

from new_app.models import Author, Post


class PostsSerializer(serializers.ModelSerializer):
    # author = AuthorsSerializer()
    class Meta:
        model = Post
        fields = '__all__'


class AuthorsSerializer(serializers.ModelSerializer):
    posts = PostsSerializer(many=True)

    class Meta:
        model = Author
        fields = ['name', 'surname', 'posts']

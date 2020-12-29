from django.shortcuts import render
from rest_framework.response import Response

from new_app.serializers import AuthorsSerializer, PostsSerializer
from rest_framework.decorators import api_view
from new_app.models import Author, Post


@api_view(['GET'])
def authors(request):
    authors = Author.objects.all()
    serializer = AuthorsSerializer(authors, many=True)
    print(serializer.data)

    return Response({"authors": serializer.data})


@api_view(['GET'])
def posts(request):
    posts = Post.objects.all()
    serializer = PostsSerializer(posts, many=True)
    print(serializer.data)

    return Response({"posts": serializer.data})

from rest_framework import generics
from rest_framework.response import Response


from utils.pagination import CustomPagination
from apps.posts.models import Post
from .serializers import (
    PostSerializers,
)


class PostListAPI(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    pagination_class = CustomPagination


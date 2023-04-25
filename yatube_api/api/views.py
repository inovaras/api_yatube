from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import permissions

from posts.models import Post, Group, Comment
from rest_framework.exceptions import PermissionDenied

from .serializers import PostSerializer, GroupSerializer, CommentSerializers
from .permissions import AuthorOrReadOnly
# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    permission_classes = (AuthorOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers

    permission_classes = (AuthorOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=get_object_or_404(Post, pk=self.kwargs['post_id']))

    def get_queryset(self):
        return self.queryset.filter(post=get_object_or_404(Post, pk=self.kwargs['post_id']))

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
    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(PostViewSet, self).perform_update(serializer)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # проверка из permissions.py
    permission_classes = (AuthorOrReadOnly,)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    # проверка из permissions.py
    permission_classes = (AuthorOrReadOnly,)
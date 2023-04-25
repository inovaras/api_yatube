from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from .permissions import AuthorOrReadOnly
from posts.models import Post, Group, Comment
from .serializers import PostSerializer, GroupSerializer, CommentSerializers


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
        serializer.save(
            author=self.request.user,
            post=get_object_or_404(Post, pk=self.kwargs['post_id']),
        )

    def get_queryset(self):
        return self.queryset.filter(
            post=get_object_or_404(Post, pk=self.kwargs['post_id'])
        )

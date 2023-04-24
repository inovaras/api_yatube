from rest_framework import serializers
from posts.models import Post, Group, Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = {'id', 'title', 'slug', 'descriptions'}


class PostSerializer(serializers.ModelSerializer):
    # author - не разрешать менять автора

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'image',  'group', 'pub_date')


class CommentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = {'id', 'author', 'post', 'text', 'created'}

from datetime import datetime
from rest_framework import serializers

from blog.models import Author, Post, Comment


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["name", "last_name", "email", "nick", "post_number", "comments_number"]


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=False, read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", default=datetime.now)

    class Meta:
        model = Post
        fields = ["author", "title", "text", "created_at", "comments_number"]


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ["author", "text",]


class PostDetailsSerializer(PostSerializer):
    comments = CommentSerializer(many=True)

    class Meta(PostSerializer.Meta):
        fields = PostSerializer.Meta.fields + ["comments",]

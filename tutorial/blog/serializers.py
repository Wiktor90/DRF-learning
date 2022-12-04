from rest_framework import serializers

from blog.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["name", "last_name", "email", "nick", "post_number", "comments_number"]

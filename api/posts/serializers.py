from rest_framework import serializers
from api.models import Post, Comment
from api.models import Profile
from api.auth.serializers import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "user", "post", "text", "date_created"]


class LikeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["likes"]


class AddCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["text"]


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("user_name", "profile_picture")


class PostSerializer(serializers.ModelSerializer):
    post_comments = CommentSerializer(many=True, read_only=True)
    author = ProfileSerializer(read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "emotion",
            "post_type",
            "text",
            "post_comments",
            "author",
            "picture",
            "likes",
            "date_created",
        ]


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["post_type", "text", "picture", "emotion"]

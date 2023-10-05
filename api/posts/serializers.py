from rest_framework import serializers
from api.models import Post, Comment
from api.models import Profile
from api.auth.serializers import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "user", "post", "text", "date_created"]

    # TODO: You are inheriting from post, do you need to do this check manually
    #   Or can you use the integrity constraint resulting in a invalid serializer
    def create(self, validated_data):

        # TODO: Can you add docstring to explain what this method is doing?

        # TODO: It looks like you could reuse the super.create behavior
        #   instead of redoing everything here?
        #   I think this method can be simplified, you can investigate into it

        request = self.context.get("request")

        # Retrieve the "post" parameter from query parameters
        post_id = request.query_params.get("post")

        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            raise serializers.ValidationError({"post": "Post not found"})

        # Add the "post" to the validated data
        validated_data["post"] = post

        # Create the comment
        comment = Comment.objects.create(**validated_data)
        return comment


class LikeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        # TODO: This is a bit confusing, I would rename LikeUpdateSerializer to PostUpdateSerializer
        #   Because the model here is Post to keep it consistent
        #   Therefore, I understand that you named it LikeUpdateSerializer
        #   because only related to likes on the Post model
        #   So choose, what you think is best on this one
        model = Post
        fields = ["likes"]


# TODO: Since we have a viewset, is this still used?
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


# TODO: Please remove this serializer if unused
class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["post_type", "text", "picture", "emotion"]

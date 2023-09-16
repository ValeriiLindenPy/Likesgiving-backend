from api.models import Post, Comment
from .serializers import *
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import date, datetime, timedelta
from django.utils import timezone

from knox.auth import TokenAuthentication


class GetTodayStatistics(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        today = timezone.now().date()
        yesterday = timezone.now() - timedelta(days=1)
        love_post_amount_today = Post.objects.filter(
            date_created__date=today, post_type="love"
        ).count()
        hate_post_amount_today = Post.objects.filter(
            date_created__date=today, post_type="hate"
        ).count()
        love_post_amount_yesterday = Post.objects.filter(
            date_created__date=yesterday, post_type="love"
        ).count()
        hate_post_amount_yesterday = Post.objects.filter(
            date_created__date=yesterday, post_type="hate"
        ).count()
        return Response(
            {
                "today_loves": love_post_amount_today,
                "today_hates": hate_post_amount_today,
                "yesterday_loves": love_post_amount_yesterday,
                "yesterday_hates": hate_post_amount_yesterday,
            }
        )


class ShowAllPosts(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ShowAllPostsByType(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PostSerializer

    def get_queryset(self):
        post_type = self.kwargs.get(
            "post_type"
        )  # Assuming you are passing the post_type in the URL
        queryset = Post.objects.filter(post_type=post_type).order_by("-date_created")
        return queryset


class ShowAllPostComment(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, post_id, format=None):
        try:
            comments = Comment.objects.filter(post_id=post_id)
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)
        except Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class RemainingPostsTodayView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = (
        PostSerializer  # You can create a custom serializer for this if needed
    )

    def get(self, request, *args, **kwargs):
        # Get the current user
        user = self.request.user

        # Calculate the date range for posts (today and yesterday)
        today = timezone.now().date()
        yesterday = today - timedelta(days=1)

        # Count the number of posts created by the user today
        posts_today = Post.objects.filter(author=user, date_created__date=today).count()

        # Calculate the remaining posts for today (assuming a limit of 3 posts per day)
        remaining_posts_today = 3 - posts_today

        # Return a response with the remaining posts for today
        response_data = {
            "remaining_posts_today": remaining_posts_today,
        }
        return Response(response_data, status=status.HTTP_200_OK)


class CreatePost(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer

    def perform_create(self, serializer):
        # Get the current user
        print(self.request)

        user = self.request.user

        # Calculate the date range for posts (today and yesterday)
        today = timezone.now().date()
        yesterday = today - timedelta(days=1)

        # Count the number of posts created by the user today and yesterday
        posts_today = Post.objects.filter(author=user, date_created__date=today).count()
        posts_yesterday = Post.objects.filter(
            author=user, date_created__date=yesterday
        ).count()

        # Check if the user has already created 5 posts today
        if posts_today >= 5:
            return Response(
                {"error": "You have reached the maximum limit of 5 posts per day."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Allow the user to create the post
        serializer.save(author=user)


class AddComment(generics.CreateAPIView):
    serializer_class = AddCommentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        try:
            post = Post.objects.get(pk=kwargs["pk"])
        except Post.DoesNotExist:
            return Response(
                {"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user, post=post)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AddLike(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    queryset = Post.objects.all()
    serializer_class = LikeUpdateSerializer
    lookup_field = "pk"

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Post.DoesNotExist:
            print("Post.DoesNotExist")
            return Response(status=status.HTTP_404_NOT_FOUND)

        user_profile = request.user

        if user_profile in instance.likes.all():
            instance.likes.remove(user_profile)
        else:
            instance.likes.add(user_profile)

        # Save the instance to update the likes field
        instance.save()

        # Create a serializer instance for returning the updated data
        instance_serializer = self.get_serializer(instance)

        return Response(instance_serializer.data, status=status.HTTP_200_OK)

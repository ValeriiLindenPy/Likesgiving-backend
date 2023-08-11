from api.models import Post, Comment
from .serializers import *
from rest_framework import generics, permissions, status
from rest_framework.response import Response


class ShowAllPosts(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ShowAllPostComment(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs["pk"]
        return Comment.objects.filter(post_id=post_id)


class CreatePost(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AddComment(generics.CreateAPIView):
    serializer_class = CommentCreateSerializer

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

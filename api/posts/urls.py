from django.urls import path

from knox import views as knox_views

from .views import *


urlpatterns = [
    path("create_post/", CreatePost.as_view(), name="create-post"),
    path("add_comment/<int:pk>/", AddComment.as_view(), name="add-comment"),
    path("get_posts/", ShowAllPosts.as_view(), name="get-posts"),
    path("get_comments/<int:pk>/", ShowAllPostComment.as_view(), name="get-comments"),
]

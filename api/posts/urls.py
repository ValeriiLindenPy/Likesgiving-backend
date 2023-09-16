from django.urls import path

from knox import views as knox_views

from .views import *


urlpatterns = [
    path("create_post/", CreatePost.as_view(), name="create-post"),
    path("add_comment/<int:pk>/", AddComment.as_view(), name="add-comment"),
    path("get_posts/", ShowAllPosts.as_view(), name="get-posts"),
    path("get_comments/<int:pk>/", ShowAllPostComment.as_view(), name="get-comments"),
    path(
        "get_posts/<str:post_type>/",
        ShowAllPostsByType.as_view(),
        name="show-posts-by-type",
    ),
    path("add-like/<int:pk>/", AddLike.as_view(), name="add-like"),
    path("get_statistics/", GetTodayStatistics.as_view(), name="get-statistics"),
    path(
        "get_remaining_posts_today/",
        RemainingPostsTodayView.as_view(),
        name="get_remaining_posts_today",
    ),
]

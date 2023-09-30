from django.urls import include, path

from knox import views as knox_views

from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"post", PostViewSet, basename="post")
router.register(r"comment", CommentViewSet, basename="comment")

urlpatterns = [
    path("v1/", include(router.urls)),
    path("add_comment/<int:pk>/", AddComment.as_view(), name="add-comment"),
    path("get_comments/<int:pk>/", ShowAllPostComment.as_view(), name="get-comments"),
    path("add-like/<int:pk>/", AddLike.as_view(), name="add-like"),
    path("get_statistics/", GetTodayStatistics.as_view(), name="get-statistics"),
    path(
        "get_remaining_posts_today/",
        RemainingPostsTodayView.as_view(),
        name="get_remaining_posts_today",
    ),
]

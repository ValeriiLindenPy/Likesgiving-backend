from django.urls import include, path

# TODO: To delete if unused
from knox import views as knox_views

# TODO: Be explicit about what you import
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"post", PostViewSet, basename="post")
router.register(r"comment", CommentViewSet, basename="comment")

urlpatterns = [

    # TODO: Only add slashes if the route is considered might contain other subroutes or actions
    #   https://stackoverflow.com/questions/61547014/restful-uri-trailing-slash-or-no-trailing-slash

    path("v1/", include(router.urls)),

    # TODO: no need to keep those routes if you use a viewset for comment
    path("add_comment/<int:pk>/", AddComment.as_view(), name="add-comment"),
    path("get_comments/<int:pk>/", ShowAllPostComment.as_view(), name="get-comments"),

    # TODO: If you want to follow the restful standards, please replace
    #   add-like by likes, you can keep the same route name for now since that's only adding likes
    path("add-like/<int:pk>/", AddLike.as_view(), name="add-like"),
    # TODO: Replace get_statistics/ by stats/ or statistics/
    path("get_statistics/", GetTodayStatistics.as_view(), name="get-statistics"),
    # TODO: Use hyphens to improve the readability of urls
    #   https://medium.com/@nadinCodeHat/rest-api-naming-conventions-and-best-practices-1c4e781eb6a5#:~:text=Use%20hyphens%20(%2D)%20to%20improve,to%20long%2Dpath%20segmented%20URIs.
    path(
        "get_remaining_posts_today/",
        RemainingPostsTodayView.as_view(),
        name="get_remaining_posts_today",
    ),
]

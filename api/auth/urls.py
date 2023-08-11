from django.urls import path

from knox import views as knox_views

from .views import CreateUserView, LoginView, ManageUserView, ShowProfileData


urlpatterns = [
    path("create/", CreateUserView.as_view(), name="create"),  # register user
    path(
        "edit-profile/", ManageUserView.as_view(), name="profile"
    ),  # show profile data
    path("login/", LoginView.as_view(), name="knox_login"),  # login
    path("logout/", knox_views.LogoutView.as_view(), name="knox_logout"),  # logout
    path(
        "profile/", ShowProfileData.as_view(), name="show_profile_data"
    ),  # show user data
]

from django.urls import path

from knox import views as knox_views

from .views import *


urlpatterns = [
    path("create/", CreateUserView.as_view(), name="create"),  # register user
    path("login/", LoginView.as_view(), name="knox_login"),  # login
    path("logout/", knox_views.LogoutView.as_view(), name="knox_logout"),  # logout
    path(
        "profile/", ShowProfileData.as_view(), name="show_profile_data"
    ),  # show user data
    path(
        "edit-profile/", UpdateUserView.as_view(), name="edit_profile_data"
    ),  # edit user data
    path(
        "change_password/",
        ChangePasswordView.as_view(),
        name="auth_change_password",
    ),
    path(
        "password_reset/",
        ResetPasswordView.as_view(),
        name="password_reset",
    ),
    path(
        "password_reset_confirm/",
        ChangePasswordConfirmView.as_view(),
        name="password_reset_confirm",
    ),
]

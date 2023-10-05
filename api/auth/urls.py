from django.urls import path

from knox import views as knox_views

from .views import *


urlpatterns = [
    # TODO: to be restful, you can replace create/ by users/ here
    path("create/", CreateUserView.as_view(), name="create"),  # register user

    # TODO: Instead of reiventing the wheel, could you reuse the ObtainToken view
    #   And only customise what you need?
    #   https://github.com/encode/django-rest-framework/blob/master/rest_framework/authtoken/views.py
    path("login/", LoginView.as_view(), name="knox_login"),  # login
    path("logout/", knox_views.LogoutView.as_view(), name="knox_logout"),  # logout

    # TODO: I would name it "/users/me" or /me or /profiles/me
    #   The graph api of facebook use something similar
    #   https://developers.facebook.com/docs/graph-api/overview#me
    path(
        "profile/", ShowProfileData.as_view(), name="show_profile_data"
    ),  # show user data
    # TODO: edit-profile would be a PUT/PATCH request on /me
    path(
        "edit-profile/", UpdateUserView.as_view(), name="edit_profile_data"
    ),  # edit user data
    # TODO: You could use the same view PUT me to update the password?
    #  Else i would call it /me/change-password if you want a specific view
    path(
        "change_password/",
        ChangePasswordView.as_view(),
        name="auth_change_password",
    ),
    # TODO: Same here
    path(
        "password_reset/",
        ResetPasswordView.as_view(),
        name="password_reset",
    ),
    # TODO: Same here
    path(
        "password_reset_confirm/",
        ChangePasswordConfirmView.as_view(),
        name="password_reset_confirm",
    ),
]

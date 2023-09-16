# django imports
import json
from django.contrib.auth import login
from django.core.mail import send_mail

# rest_framework imports
from rest_framework import generics, permissions, status, views
from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework.decorators import action

# knox imports
from knox.models import AuthToken
from knox.auth import TokenAuthentication

# local apps import
from .serializers import *

from api.models import *


class CreateUserView(generics.CreateAPIView):
    # Create user API view
    serializer_class = UserSerializer


class LoginView(generics.GenericAPIView):
    # login view extending KnoxLoginView
    serializer_class = AuthSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        payload = request.data  # JSON data is directly available in request.data

        serializer = self.get_serializer(data=payload)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data
        AuthToken.objects.filter(user=user).delete()  # Remove existing tokens

        instance, token = AuthToken.objects.create(user)

        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": token,
                "id": user.id,
            }
        )


class UpdateUserView(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = UpdateUserDataSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user


class ChangePasswordView(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

    def get_object(self):
        return self.request.user


class ResetPasswordView(views.APIView):
    def post(self, request):
        # Create an instance of the serializer with the request data
        serializer = ResetPasswordSerializer(data=request.data)

        if serializer.is_valid():
            # Valid data, retrieve the email
            email = serializer.validated_data["email"]

            # Send the email
            try:
                user = Profile.objects.get(email=email)
                instance, token = AuthToken.objects.create(user)
                reset_link = (
                    f"http://localhost:4000/password-change-confirm?token={token}"
                )
                sent_mail = send_mail(
                    "Reset Password",
                    f"Click the following link to reset your password: {reset_link}",
                    from_email=None,
                    recipient_list=[email],
                    fail_silently=False,
                )

                return Response(
                    {"msg": f"Email sent successfully: {sent_mail}"},
                    status=status.HTTP_200_OK,
                )

            except Exception as e:
                return Response(
                    {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        else:
            # Invalid data, return validation errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from django.contrib.auth.hashers import make_password


class ChangePasswordConfirmView(generics.UpdateAPIView):
    serializer_class = ChangePasswordConfirmSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = (permissions.IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        # Get the user making the request
        user = request.user

        # Get the new password from the request data
        new_password = request.data.get("password")

        # Update the user's password
        user.password = make_password(new_password)
        user.save()

        # Remove the user's token from Knox database
        AuthToken.objects.filter(user=user).delete()

        return Response(
            {"message": "Password updated and token removed successfully"},
            status=status.HTTP_200_OK,
        )


class ShowProfileData(generics.GenericAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        # Get the profile for the currently authenticated user
        profile = Profile.objects.get(email=request.user.email)
        serializer = self.get_serializer(instance=profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

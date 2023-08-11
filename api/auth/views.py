# django imports
from django.contrib.auth import login

# rest_framework imports
from rest_framework import generics, permissions, status
from rest_framework.settings import api_settings
from rest_framework.response import Response


# knox imports
from knox.models import AuthToken
from knox.auth import TokenAuthentication

# local apps import
from .serializers import *


class CreateUserView(generics.CreateAPIView):
    # Create user API view
    serializer_class = UserSerializer


class LoginView(generics.GenericAPIView):
    # login view extending KnoxLoginView
    serializer_class = AuthSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1],
            }
        )


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""

    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authenticated user"""
        return self.request.user


class ShowProfileData(generics.GenericAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        # Get the profile for the currently authenticated user
        profile = Profile.objects.get(email=request.user.email)
        serializer = self.get_serializer(instance=profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

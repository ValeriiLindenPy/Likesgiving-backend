from api.models import Profile
from django.contrib.auth import authenticate, get_user_model

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """serializer for the user object"""

    class Meta:
        model = Profile
        fields = ("email", "user_name", "password")
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}

    def create(self, validated_data):
        return Profile.objects.create_user(**validated_data)


class AuthSerializer(serializers.Serializer):
    """serializer for the user authentication object"""

    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid Details.")


class UserDetailSerializer(serializers.ModelSerializer):
    """serializer for show user data"""

    class Meta:
        model = Profile
        exclude = ("password",)

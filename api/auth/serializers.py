from api.models import Profile
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth import password_validation
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """serializer for the user object"""

    class Meta:
        model = Profile
        fields = ("email", "user_name", "password", "profile_picture")
        extra_kwargs = {"password": {"write_only": True, "min_length": 10}}

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


class UpdateUserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("user_name", "email", "profile_picture")
        extra_kwargs = {
            "user_name": {"required": False},
            "email": {"required": False},
            "profile_picture": {"required": False},
        }


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[password_validation.validate_password],
    )
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Profile
        fields = ("old_password", "password", "password2")

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        return attrs

    def validate_old_password(self, value):
        user = self.context["request"].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                {"old_password": "Old password is not correct"}
            )
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data["password"])
        instance.save()

        return instance


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ChangePasswordConfirmSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True)

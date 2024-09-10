from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from .validators import (
    CustomPasswordValidator,
    CustomProfileDeleteValidator,
    CustomBirthdayValidator,
)


class SignupSerializer(CustomBirthdayValidator, serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "password",
            "username",
            "email",
            "name",
            "nickname",
            "birthday",
            "sex",
            "introduce",
        )


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        exclude = (
            "groups",
            "user_permissions",
            "is_staff",
            "is_active",
            "is_superuser",
            "password",
            "username",
        )
        read_only_fields = (
            "date_joined",
            "last_login",
        )


class ProfileDeleteSerializer(
    CustomProfileDeleteValidator, serializers.ModelSerializer
):
    check_password = serializers.CharField(write_only=True, required=True)
    refresh = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = get_user_model()
        fields = ("check_password", "refresh")


class PasswordChangeSerializer(CustomPasswordValidator, serializers.ModelSerializer):
    password1 = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = get_user_model()
        fields = ("password1", "password2", "old_password")

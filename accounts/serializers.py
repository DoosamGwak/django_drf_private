from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from .validators import CustomPasswordValidator, CustomProfileDeleteValidator


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        exclude = (
            "groups",
            "user_permissions",
            "last_login",
            "date_joined",
        )


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        exclude = (
            "groups",
            "user_permissions",
        )
        read_only_fields = (
            "is_staff",
            "is_active",
            "is_superuser",
            "last_login",
            "date_joined",
        )


class ProfileDeleteSerializer(
    CustomProfileDeleteValidator, serializers.ModelSerializer
):
    check_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = get_user_model()
        fields = ("check_password",)


class PasswordChangeSerializer(CustomPasswordValidator, serializers.ModelSerializer):
    password1 = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = get_user_model()
        fields = ("password1", "password2", "old_password")

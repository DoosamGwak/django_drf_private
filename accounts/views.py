from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    UpdateAPIView,
    CreateAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView,
)
from .serializers import (
    SignupSerializer,
    ProfileSerializer,
    ProfileDeleteSerializer,
    PasswordChangeSerializer,
)
from .models import User
from .permissions import OwnerOnly


class SignupView(CreateAPIView):
    serializer_class = SignupSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()


class ProfileView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (
        IsAuthenticated,
        OwnerOnly,
    )
    serializer_class = ProfileSerializer
    lookup_field = "username"


class ProfileDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = (
        IsAuthenticated,
        OwnerOnly,
    )
    serializer_class = ProfileDeleteSerializer

    def get_object(self):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = self.get_object()
        self.perform_destroy(user)
        return Response(
            {"msg": "성공적으로 회원탈퇴 되었습니다."},
            status=status.HTTP_204_NO_CONTENT,
        )

    def perform_destroy(self, instance):
        instance.delete()


class PasswordChangeView(UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (
        IsAuthenticated,
        OwnerOnly,
    )
    serializer_class = PasswordChangeSerializer

    def get_object(self):
        return self.request.user


class FollowView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, username):
        target_user = get_object_or_404(User, username=username)
        user = request.user
        if user == target_user:
            return Response(
                {"msg": "자신을 대상으로 지정할 수 없습니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if not target_user in user.followings.all():
            user.followings.add(target_user)
            return Response({"msg": "팔로우하셨습니다."}, status=status.HTTP_200_OK)
        return Response(
            {"msg": "이미 팔로우 하셨습니다."}, status=status.HTTP_204_NO_CONTENT
        )

    def delete(self, request, username):
        target_user = get_object_or_404(User, username=username)
        user = request.user

        if user == target_user:
            return Response(
                {"msg": "자신을 대상으로 지정할 수 없습니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if target_user in user.followings.all():
            user.followings.remove(target_user)
            return Response(
                {"msg": "팔로우를 취소하였습니다."}, status=status.HTTP_204_NO_CONTENT
            )
        return Response(
            {"msg": "해당 유저를 팔로우하지 않았습니다."},
            status=status.HTTP_204_NO_CONTENT,
        )

from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)
from .views import (
    SignupView,
    ProfileView,
    PasswordChangeView,
    ProfileDeleteView,
    FollowView,
)


app_name = "accounts"
urlpatterns = [
    path("", SignupView.as_view(), name="signup"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("logout/", TokenBlacklistView.as_view(), name="logout"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("profile/", ProfileDeleteView.as_view(), name="profile_delete"),
    path("profile/<str:username>/", ProfileView.as_view(), name="profile"),
    path("password/", PasswordChangeView.as_view(), name="password"),
    path("follow/<str:username>/", FollowView.as_view(), name="follow"),
]

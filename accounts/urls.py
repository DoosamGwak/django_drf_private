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
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("logout/", TokenBlacklistView.as_view(), name="logout"),
    path("", SignupView.as_view(), name="signup"),
    path("profile/", ProfileDeleteView.as_view(), name="profile_delete"),
    path("profile/<str:username>/", ProfileView.as_view(), name="profile"),
    path("password/<str:username>/", PasswordChangeView.as_view(), name="password"),
    path("follow/<str:username>/", FollowView.as_view(), name="follow"),
]

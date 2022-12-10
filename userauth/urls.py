from django.urls import path, include
from .views import (
    UserLoginView,
    UserProfileView,
    UserRegistrationView,
)
urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="user_registration"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("userprofile/", UserProfileView.as_view(), name="profile")
]
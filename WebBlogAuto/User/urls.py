from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login/", login_request, name = "login"),
    path("register/", register, name = "register"),
    path("logout/", LogoutView.as_view(), name = "logout"),
]
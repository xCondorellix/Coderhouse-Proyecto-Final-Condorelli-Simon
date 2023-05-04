from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("login/", login_request, name = "login"),
    path("register/", register, name = "register"),
]
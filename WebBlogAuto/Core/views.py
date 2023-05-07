from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from User import views

# Create your views here.

@login_required
def home(request):
    return render(request, "Core/home.html")
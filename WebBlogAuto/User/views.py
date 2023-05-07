from django.shortcuts import render
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView

from Core import templates

# Create your views here.

def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            info=form.cleaned_data
            
            usu=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usu, password=clave,)

            if usuario is not None:
                login(request, usuario)
                return render(request, "Core/home.html", {"mensaje":f"Usuario {usu} logueado correctamente"})
            else:
                return render(request, "User/login.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
        else:
            return render(request, "User/login.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
    else:
        form=AuthenticationForm()
        return render(request, "User/login.html", {"form": form})
    
def register(request):

    if request.method =="POST":
        form = RegistroUsuarioForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "Core/home.html", {"mensaje": "Usuario creado correctamente!"})
        else:
            return render(request, "User/register.html", {"form": form, "mensaje":"Error al crear el usuario"})            

    else:
        form = RegistroUsuarioForm()
        return render (request, "User/register.html", {"form": form}) 

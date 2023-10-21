from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout,authenticate
from Acceso.forms import UserRegisterForm, UserEditForm
from django.contrib.auth.decorators import login_required
from .models import Avatar


def login_request(request):
    
    form = AuthenticationForm(request, data=request.POST)
    
    if request.method == "POST":
        if form.is_valid():
            user = form.cleaned_data.get('username')
            psw = form.cleaned_data.get('password')
            
            user_fin= authenticate(username = user, password = psw)
            
            if user_fin is not None:
                login(request,user_fin)
                
                return render(request, "AppKalos/index.html", {f"name":{user},"mensaje":f"Bienvenido {user}"})
            else:
                return render(request, "Acceso/login.html", {"mensaje":"Error, datos incorrectos"})
        else:
             return render(request, "Acceso/login.html", {"mensaje":"Error, formulario erroneo"})

    form = AuthenticationForm()

    return render(request,"Acceso/login.html", {'form':form})
            
def register (request):
    if request.method == "POST":
        
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user= form.cleaned_data['username']
            form.save()
            return render (request, "AppKalos/index.html", {"mensaje": f"{user}, Usuario Creado"})
    
    else:
        form = UserRegisterForm()
    
    return render(request, "Acceso/register.html", {"form": form})

@login_required
def edit_profile(request):
    user = request.user
    
    if request.method == "POST":
        
        miFormulario = UserEditForm(request.POST)
        
        if miFormulario.is_valid():    
            
            informacion = miFormulario.cleaned_data
            
            if informacion["password1"] != informacion["password2"]:
                datos = {
                    'first_name': user.first_name,
                    'email':user.email
                }
                miFormulario = UserEditForm(initial=datos)
            else:    
                user.email = informacion['email']
                user.set_password = informacion['password1']
                user.first_name = informacion['first_name']
                user.last_name = informacion['last_name']
                
                user.save()
            
                return render(request, "AppKalos/index.html")
    
    else:
        datos = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email':user.email
        }
        
        miFormulario= UserEditForm(initial=datos)
    
    return render(request, "Acceso/edit_profile.html", {"miFormulario":miFormulario, "user":user})



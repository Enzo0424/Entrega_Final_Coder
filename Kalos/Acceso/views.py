from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.views import PasswordChangeView
from Acceso.forms import UserRegisterForm, UserEditForm, PasswordChangeCustomForm
from django.contrib.auth.decorators import login_required
from Acceso.models import Avatar
from django.contrib import messages


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
    usuario = request.user

    if request.method == "POST":
        miFormulario = UserEditForm(request.POST, request.FILES)
        
        if miFormulario.is_valid():    
            informacion = miFormulario.cleaned_data
            
            usuario.email = informacion['email']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            usuario.save()
                
            try:
                avatar = Avatar.objects.get(user=usuario)
            except Avatar.DoesNotExist:
                avatar = Avatar(user=usuario)

            if 'imagen' in request.FILES:
                avatar.imagen = request.FILES['imagen']

            avatar.save()
                
            return render(request, "AppKalos/index.html")
    
    else:
        datos = {
            'email': usuario.email,
            'first_name': usuario.first_name,
            'last_name': usuario.last_name
        }
        
        miFormulario = UserEditForm(initial=datos)
    
    return render(request, "Acceso/edit_profile.html", {"miFormulario": miFormulario, "user": usuario})


@login_required
def profile_view(request):
    user = request.user
    return render(request, 'Acceso/profile_view.html', {'user': user})

from django.contrib.auth.forms import PasswordChangeForm

@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeCustomForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Importante para mantener la sesión del usuario
            messages.success(request, "Contraseña cambiada con éxito.")
            return redirect('profile_view')
        else:
            messages.error(request, "Por favor, corrige los errores a continuación.")
    else:
        form = PasswordChangeCustomForm(request.user)

    return render(request, 'Acceso/change_password.html', {'form': form})



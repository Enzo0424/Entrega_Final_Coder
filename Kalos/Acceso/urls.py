from django.urls import path
from Acceso.views import login_request, register,edit_profile
from django.contrib.auth.views import LogoutView


urlpatterns = [

    path('login', login_request, name="Login"),
    path('register', register, name="Register"),
    path('logout', LogoutView.as_view(template_name="Acceso/logout.html"), name="Logout"),
    path('editarPerfil', edit_profile, name="Edit_Profile"),
   ]

from django.shortcuts import render
from django.http import HttpResponse
from AppKalos.models import Pacientes
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Inicio(ListView):
    model = Pacientes
    template_name = "AppKalos/index.html"

class PacientesInicio(LoginRequiredMixin,ListView):
    model = Pacientes
    template_name = "AppKalos/pacientes.html"

class PacientesListView(LoginRequiredMixin,ListView):
    model = Pacientes
    template_name = "AppKalos/pacientes_list.html"

class PacientesDetailView(LoginRequiredMixin,DetailView):
    model = Pacientes
    template_name = "AppKalos/pacientes_detail.html"

class PacientesCreateView(LoginRequiredMixin,CreateView):
    model = Pacientes
    success_url = reverse_lazy("List")
    fields = ['nombre','apellido','dni','prestadora']

class PacientesUpdateView (LoginRequiredMixin,UpdateView):
    model = Pacientes
    template_name = "AppKalos/pacientes_edit.html"
    success_url = reverse_lazy("List")
    fields = ['id','nombre','apellido','dni','prestadora']
    
class PacientesDeleteView (LoginRequiredMixin,DeleteView):
    model = Pacientes
    success_url = reverse_lazy("List") 
    template_name = "AppKalos/pacientes_delete.html" #Ver, no iría
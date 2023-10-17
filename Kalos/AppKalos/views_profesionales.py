from django.shortcuts import render
from django.http import HttpResponse
from AppKalos.models import Profesionales
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ProfesionalesInicio(LoginRequiredMixin,ListView):
    model = Profesionales
    template_name = "AppKalos/profesionales/profesionales.html"

class ProfesionalesListView(LoginRequiredMixin,ListView):
    model = Profesionales
    template_name = "AppKalos/profesionales/profesionales_list.html"

class ProfesionalesDetailView(LoginRequiredMixin,DetailView):
    model = Profesionales
    template_name = "AppKalos/profesionales/profesionales_detail.html"

class ProfesionalesCreateView(LoginRequiredMixin,CreateView):
     model = Profesionales
     template_name = "AppKalos/profesionales/profesionales_form.html"
     success_url = reverse_lazy("ListProf")
     fields = ['nombre','apellido','dni','profesion']

class ProfesionalesUpdateView (LoginRequiredMixin,UpdateView):
     model = Profesionales
     template_name = "AppKalos/profesionales/profesionales_edit.html"
     success_url = reverse_lazy("ListProf")
     fields = ['id','nombre','apellido','dni','profesion']
    
class ProfesionalesDeleteView (LoginRequiredMixin,DeleteView):
     model = Profesionales
     success_url = reverse_lazy("List") 
     template_name = "AppKalos/profesionales/profesionales_delete.html" #Ver, no iría
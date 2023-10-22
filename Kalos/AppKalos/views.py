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
    template_name = "AppKalos/index.html"
    model = Pacientes
class About(ListView):
    template_name = "AppKalos/about/about_me.html"
    model = Pacientes
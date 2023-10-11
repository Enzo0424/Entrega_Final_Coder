from django.urls import path
from AppKalos.views import inicio, paciente, pacientes_form,buscar_pacientes


urlpatterns = [
    path('Inicio/', inicio, name= "Inicio"),
    path('Pacientes/', paciente, name="Pacientes"),
    path('Pacientesform/', pacientes_form, name="Carga de Pacientes"),
    path('Buscar_Pacientes/', buscar_pacientes, name="Buscar Pacientes"),
]
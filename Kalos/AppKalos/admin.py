from django.contrib import admin
from .models import Pacientes, Profesionales
# Register your models here.

admin.site.register(Pacientes)
admin.site.register(Profesionales)
from django.db import models

# Create your models here.
class Pacientes (models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.CharField(max_length=8, unique=True)
    prestadora = models.CharField(max_length=20)
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - DNI: {self.dni} - Prestadora: {self.prestadora}"
    
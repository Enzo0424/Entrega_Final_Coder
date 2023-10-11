from django import forms

class PacienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    dni = forms.IntegerField()
    prestadora = forms.CharField(max_length=20)
    
class BuscarPaciente(forms.Form):
    dni = forms.IntegerField()
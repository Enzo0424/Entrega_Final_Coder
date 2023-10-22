from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}
        


def validate_image_extension(value):
    """
    Valida que el archivo sea una imagen (extensiones permitidas: jpg, jpeg, png, gif).
    """
    allowed_extensions = ('.jpg', '.jpeg', '.png', '.gif')
    if not value.name.lower().endswith(allowed_extensions):
        raise ValidationError('Solo se permiten archivos de imagen (jpg, jpeg, png, gif).')

class UserEditForm(forms.Form):

    # Obligatorios
    email = forms.EmailField(label="Ingrese su email:")
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    imagen = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

    imagen = forms.ImageField(required=False, validators=[validate_image_extension])

    def clean_imagen(self):
        imagen = self.cleaned_data.get('imagen')
        if imagen:
            validate_image_extension(imagen)
        return imagen

class PasswordChangeCustomForm(PasswordChangeForm):
    class Meta:
        model = User

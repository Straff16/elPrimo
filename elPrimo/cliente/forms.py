from django import forms
from tienda.models import Usuario

MUNICIPIOS = (
    ('Bejuma', 'Bejuma'),
    ('Valencia', 'Valencia'),
    ('San Diego', 'San Diego'),
    ('Guacara', 'Guacara'),
    ('Los Guayos', 'Los Guayos'),
)

class RegisterForm(forms.Form):

    usuario = forms.CharField(max_length=65, required=True)
    correo = forms.CharField(max_length=65, widget=forms.EmailInput, required=True)
    #cedula = forms.CharField(max_length=8)
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput, label='Contraseña', required=True)
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput, label='Confirmar contraseña', required=True)

    

class LoginForm(forms.Form):
    
    usuario = forms.CharField(max_length=65, required=True,)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput, required=True, label='Contraseña')

class UpdateForm(forms.Form):
    municipio = forms.ChoiceField(choices=MUNICIPIOS)
    urbanizacion = forms.CharField(max_length=50, required=True)
    telefono = forms.CharField(required=True)
    cedula = forms.CharField(max_length=12, required=True)
    direccion = forms.CharField(max_length=120, required=True)

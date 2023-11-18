from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
#Formularios creados para hacer el registro de objetos en cada modelo en el sitio web.
class AbandonadosFormulario(forms.Form):
    titulo=forms.CharField()
    autor=forms.CharField()
    año_publicacion=forms.CharField()
class LeidosFormulario(forms.Form):
    titulo=forms.CharField()
    autor=forms.CharField()
    año_publicacion=forms.CharField()
class LeyendoFormulario(forms.Form):
    titulo=forms.CharField()
    autor=forms.CharField()
    año_publicacion=forms.CharField()
class PorLeerFormulario(forms.Form):
    titulo=forms.CharField()
    autor=forms.CharField()
    año_publicacion=forms.CharField()
class UserEditForm(UserChangeForm):
    password= None
    username=forms.CharField()
   

    class Meta:
        model = User
        fields=['username']


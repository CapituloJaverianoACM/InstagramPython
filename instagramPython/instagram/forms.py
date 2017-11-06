from django.core.exceptions import ValidationError
from django import forms
from .models import *
from django.contrib.auth.models import User

class UserForm(forms.Form):
    email = forms.EmailField( widget=forms.EmailInput )
    name = forms.CharField()
    username = forms.CharField()
    password = forms.CharField( widget=forms.PasswordInput )
    email.widget.attrs.update({'class':'form-control',
                                'placeholder':'Correo Electrónico'})
    name.widget.attrs.update({'class':'form-control',
                                'placeholder':'Nombre Completo'})
    username.widget.attrs.update({'class':'form-control',
                                'placeholder':'Nombre de Usuario'})
    password.widget.attrs.update({'class':'form-control',
                                'placeholder':'Contraseña'})
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email = email).exists():
            raise ValidationError("El correo electrónico ya está en uso.")
        return email
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username = username).exists():
            raise ValidationError("El nombre de usuario ya está en uso.")
        return username



class PostForm(forms.Form):
    photo = forms.FileField()
    description = forms.CharField( widget=forms.Textarea )
    photo.widget.attrs.update({'id':'imgInp'})
    description.widget.attrs.update({'class':'form-control',
                                    'placeholder':'Añade la descripcion...',
                                    'rows':3})

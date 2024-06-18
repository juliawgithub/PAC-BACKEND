# forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import Login

class LoginForm(forms.ModelForm):
    MUNICIPIOS_CHOICES = [
        ('Corupá', 'Corupá'),
        ('Jaraguá do Sul', 'Jaraguá do Sul'),
        ('Schroeder', 'Schroeder'),
        ('Guaramirim', 'Guaramirim'),
        ('Masaranduba', 'Masaranduba'),
        ('São João do Itaperiu', 'São João do Itaperiu'),
        ('Barra Velha', 'Barra Velha'),
    ]
    municipio = forms.ChoiceField(choices=MUNICIPIOS_CHOICES)

    class Meta:
        model = Login
        fields = ['entidade', 'email', 'senha', 'municipio']
        widgets = {
            'senha': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get('senha')

        # Validar se a senha possui pelo menos 8 caracteres
        if len(senha) < 8:
            raise forms.ValidationError("A senha deve conter pelo menos 8 caracteres.")

        return cleaned_data

    def save(self, commit=True):
        login_instance = super().save(commit=False)
        login_instance.senha = make_password(self.cleaned_data['senha'])
        if commit:
            login_instance.save()
        return login_instance

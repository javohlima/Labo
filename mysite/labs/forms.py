from .models import Project
from django.forms import ModelForm, TextInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["title", "project"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "task": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
        }


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
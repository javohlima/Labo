from django.shortcuts import render, redirect
from .models import *
from .forms import ProjectForm
from . import forms


def index(request):
    projects = Project.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница', 'projects': projects})


def about(request):
    return render(request, 'main/about.html')


def list(request):
    form = ProjectForm()
    context = {
        'form': form
    }
    return render(request, 'main/list.html', context)


def sponsors(request):
    return render(request, 'main/sponsors.html')


def register(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = forms.RegisterForm()

    return render(request, 'registration/registr.html', {'form': form})

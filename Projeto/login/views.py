# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .models import Login
from plano.models import Plano  # Certifique-se de importar corretamente o modelo Plano
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login_instance = form.save(commit=False)
            user = User.objects.create_user(username=form.cleaned_data['email'], email=form.cleaned_data['email'], password=form.cleaned_data['senha'])
            login_instance.user = user
            login_instance.save()
            user = authenticate(request, email=form.cleaned_data['email'], password=form.cleaned_data['senha'])
            if user is not None:
                login(request, user)
                return redirect('plano/templates/index.html')  # Substitua 'index.html' pelo seu URL desejado após o login
    else:
        form = LoginForm()

    return render(request, 'login/login.html', {'form': form})

def login_success(request):
    user = request.user
    if user.is_authenticated and hasattr(user, 'login'):
        municipio = user.login.municipio
        planos = Plano.objects.filter(municipio=municipio)
        return render(request, 'plano/templates/index.html', {'planos': planos})
    else:
        return render(request, 'error.html', {'message': 'Usuário não autenticado ou município não encontrado'})

def municipio_view(request, municipio):
    planos = Plano.objects.filter(municipio=municipio)
    context = {
        'municipio': municipio,
        'planos': planos,
    }
    return render(request, 'login/municipio.html', context)

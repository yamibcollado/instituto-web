from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import RegistroForm
from django.contrib import messages

# Registro

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro exitoso")
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'registro/registro.html', {'form': form})

# Login
def login_usuario(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Inicio de sesión exitoso")
            return redirect('home')
        else:
            messages.error(request, "Usuario o contraseña incorrectos")
    else:
        form = AuthenticationForm()
    return render(request, 'registro/login.html', {'form': form})

# Logout
def logout_usuario(request):
    logout(request)
    messages.info(request, "Has cerrado sesión")
    return redirect('home')

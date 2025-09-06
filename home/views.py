from django.shortcuts import render

from usuarios.models import Usuario


# Create your views here.

def home(request):
    usuarios = Usuario.objects.all()
    
    for usuario in usuarios:
        print(usuario)
        for grupo in usuario.groups.all():
            print(f" - Grupo: {grupo.name}")

    return render(request, "home/home.html")

def nosotros(request):
    return render(request, 'home/nosotros.html')
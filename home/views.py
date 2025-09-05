from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, "home/home.html")

def nosotros(request):
    return render(request, 'home/nosotros.html')
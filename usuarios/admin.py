from django.contrib import admin
from .models import Alumno, Profesor, Administrador

admin.site.register(Alumno)
admin.site.register(Profesor)
admin.site.register(Administrador)

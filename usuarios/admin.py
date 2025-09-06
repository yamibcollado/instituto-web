from django.contrib import admin
from .models import  PerfilAdministrador, PerfilAlumno, PerfilProfesor, Usuario

admin.site.register(PerfilAlumno)
admin.site.register(PerfilProfesor)
admin.site.register(PerfilAdministrador)
admin.site.register(Usuario)


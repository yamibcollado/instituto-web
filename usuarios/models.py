from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    documento = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Alumno(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_full_name()

class Profesor(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=50)

    def __str__(self):
        return self.user.get_full_name()

class Administrador(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.get_full_name()

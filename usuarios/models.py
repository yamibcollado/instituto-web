from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin, Group)
from django.db import models


    
class UserManager(BaseUserManager):
    def create_user(self, documento, password=None, **extra_fields): # Cambiado de email a documento
        """
        Crea y guarda un Usuario con el documento y contraseña dados.
        """
        if not documento:
            raise ValueError('El usuario debe tener un documento.')

        # Ya no se normaliza el email aquí, porque no es el username
        user = self.model(documento=documento, **extra_fields) 
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, documento, password=None, **extra_fields): # Cambiado de email a documento
        """
        Crea y guarda un superusuario con el documento y contraseña dados.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(documento, password, **extra_fields) # Pasa el documento


class Usuario(AbstractBaseUser, PermissionsMixin):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    documento = models.IntegerField(blank=True, null=True, unique=True)
    grupo_activo = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    
    USERNAME_FIELD = 'documento'
    REQUIRED_FIELDS = ['nombre', 'apellido']
    objects = UserManager()

    def get_full_name(self):
        return f"{self.nombre} {self.apellido}"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class PerfilAlumno(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='perfil_alumno')

    def __str__(self):
        return self.user.get_full_name()

class PerfilProfesor(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='perfil_profesor')
    especialidad = models.CharField(max_length=50)

    def __str__(self):
        return self.user.get_full_name()

class PerfilAdministrador(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='perfil_administrador')
    cargo = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.get_full_name()

from django.db import models
from usuarios.models import Usuario

class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    profesor = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name='cursos_profesor')
    imagen = models.ImageField(upload_to='cursos/', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Inscripcion(models.Model):
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('abandono', 'Abandono'),
        ('finalizado', 'Finalizado'),
    ]

    alumno = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='inscripciones_alumno')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='inscripciones_curso')
    fecha_inscripcion = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='activo')

    class Meta:
        unique_together = ('alumno', 'curso')

    def __str__(self):
        return f"{self.alumno.get_full_name()} - {self.curso.nombre}"



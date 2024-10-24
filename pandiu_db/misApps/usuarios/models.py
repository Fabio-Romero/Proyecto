from django.db import models
from misApps.facultades.models import Programa

class TipoUsuario(models.Model):
    name = models.CharField(max_length=50)  # Ej: Estudiante, Docente, Investigador

    def __str__(self):
        return self.name

class Usuario(models.Model):
    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    program = models.ForeignKey(Programa, on_delete=models.CASCADE, null=True, blank=True)
    tipos_usuario = models.ManyToManyField(TipoUsuario, through='UsuarioTipoUsuario')

    def __str__(self):
        return f'{self.name} {self.lastName}'

class UsuarioTipoUsuario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.usuario} - {self.tipo_usuario}'


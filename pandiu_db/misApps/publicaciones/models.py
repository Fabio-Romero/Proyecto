from django.db import models
from misApps.usuarios.models import Usuario
from misApps.gruposDeInvestigacion.models import GrupoInvestigacion

class TipoPublicacion(models.Model):
    nombre_tipo = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre_tipo



class PalabraClave(models.Model):
    palabra = models.CharField(max_length=100)

    def __str__(self):
        return self.palabra

class Publicacion(models.Model):
    titulo = models.CharField(max_length=255)
    resumen = models.TextField()
    fecha_publicacion = models.DateField()
    archivo_pdf = models.FileField(upload_to='publicaciones/pdf/', null=True, blank=True)  # Nuevo campo
    grupo_investigacion = models.ForeignKey(GrupoInvestigacion, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipos_publicacion = models.ForeignKey(TipoPublicacion, null=True,  on_delete=models.CASCADE)
    palabras_clave = models.ManyToManyField(PalabraClave, through='PublicacionPalabraClave')

    def __str__(self):
        return self.titulo


class PublicacionPalabraClave(models.Model):
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    palabra_clave = models.ForeignKey(PalabraClave, on_delete=models.CASCADE)

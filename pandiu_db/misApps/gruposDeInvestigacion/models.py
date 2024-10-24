from django.db import models

class GrupoInvestigacion(models.Model):
    nombre_grupo = models.CharField(max_length=255)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre_grupo

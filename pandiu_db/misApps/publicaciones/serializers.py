from rest_framework import serializers
from misApps.publicaciones.models import Publicacion, TipoPublicacion, PalabraClave, PublicacionPalabraClave
from misApps.gruposDeInvestigacion.serializers import GrupoInvestigacionSerializer
from misApps.usuarios.serializers import UsuarioSerializer
from misApps.gruposDeInvestigacion.models import GrupoInvestigacion
from misApps.usuarios.models import Usuario
class TipoPublicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPublicacion
        fields = ("__all__")


class PalabraClaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = PalabraClave
        fields = ("__all__")



class PublicacionPalabraClaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicacionPalabraClave
        fields = ("__all__")

class PublicacionSerializer(serializers.ModelSerializer):
    tipos_publicacion = serializers.PrimaryKeyRelatedField(
        queryset=TipoPublicacion.objects.all(),
        write_only=True
    )
    
    palabras_clave = serializers.PrimaryKeyRelatedField(
        queryset=PalabraClave.objects.all(),
        many=True,
        write_only=True
    )
    
    grupo_investigacion = serializers.PrimaryKeyRelatedField(
        queryset=GrupoInvestigacion.objects.all(),
        write_only=True
    )
    
    usuario = serializers.PrimaryKeyRelatedField(
        queryset=Usuario.objects.all(),
        write_only=True
    )

    # Campos para la respuesta
    tipos_publicacion_info = TipoPublicacionSerializer(source='tipos_publicacion', read_only=True)
    palabras_clave_info = PalabraClaveSerializer(many=True, source='palabras_clave', read_only=True)
    grupo_investigacion_info = GrupoInvestigacionSerializer(source='grupo_investigacion', read_only=True)
    usuario_info = UsuarioSerializer(source='usuario', read_only=True)

    class Meta:
        model = Publicacion
        fields = (
            'id',
            'titulo',
            'resumen',
            'fecha_publicacion',
            'archivo_pdf',
            'tipos_publicacion',  # Solo ID para escritura
            'tipos_publicacion_info',  # Información completa para lectura
            'palabras_clave',  # Solo ID para escritura
            'palabras_clave_info',  # Información completa para lectura
            'grupo_investigacion',  # Solo ID para escritura
            'grupo_investigacion_info',  # Información completa para lectura
            'usuario',  # Solo ID para escritura
            'usuario_info',  # Información completa para lectura
        )
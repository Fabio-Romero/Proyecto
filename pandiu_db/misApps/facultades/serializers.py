from rest_framework import serializers
from misApps.facultades.models import Facultad, Programa

# Serializer para Facultad
class FacultadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facultad
        fields = ("__all__")

# Serializer para Programa
class ProgramaSerializer(serializers.ModelSerializer):
    facultad_nombre = serializers.SerializerMethodField()
    
    # Campo solo para escritura (POST/PUT), acepta solo el id
    facultad = serializers.PrimaryKeyRelatedField(
        queryset=Facultad.objects.all(),
        write_only=True
    )

    class Meta:
        model = Programa
        fields = ('id', 'program_name', 'facultad', 'facultad_nombre')

    def get_facultad_nombre(self, obj):
        return {
            "id": obj.facultad.id,
            "nombre_facultad": obj.facultad.nombre_facultad
        }

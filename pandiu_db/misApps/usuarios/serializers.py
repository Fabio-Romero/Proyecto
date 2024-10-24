from rest_framework import serializers
from misApps.usuarios.models import Usuario, TipoUsuario, UsuarioTipoUsuario
from misApps.facultades.serializers import ProgramaSerializer
from misApps.facultades.models import Programa
# Serializer para TipoUsuario
class TipoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoUsuario
        fields = "__all__"

# Serializer para UsuarioTipoUsuario (modelo intermedio)
class UsuarioTipoUsuarioSerializer(serializers.ModelSerializer):
    tipo_usuario = TipoUsuarioSerializer(read_only=True)  # Serializa el TipoUsuario
    usuario = serializers.PrimaryKeyRelatedField(read_only=True)  # Agrega el campo usuario como PK

    class Meta:
        model = UsuarioTipoUsuario
        fields = ["usuario", "tipo_usuario"]

# Serializer para Usuario
class UsuarioSerializer(serializers.ModelSerializer):
    # Usamos PrimaryKeyRelatedField para la creación 
    tipos_usuario = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=TipoUsuario.objects.all()
    )
    # Usamos el serializer para Programa
    name_program = serializers.SerializerMethodField()
    program = serializers.PrimaryKeyRelatedField(
        queryset=Programa.objects.all(),
        write_only=True
    )
    
    class Meta:
        model = Usuario
        fields = ("id", "name", "lastName", "email", "program","name_program", "tipos_usuario")

    def create(self, validated_data):
        tipos_usuario_data = validated_data.pop('tipos_usuario')
        usuario = Usuario.objects.create(**validated_data)
        
        for tipo in tipos_usuario_data:
            UsuarioTipoUsuario.objects.create(usuario=usuario, tipo_usuario=tipo)
        
        return usuario
    
    
    def get_name_program(self, obj):
        
        return {
        "id": obj.program.id,
        "program_name": obj.program.program_name,
    }
    # Este método se usa para devolver los tipos de usuario completos (ID y name) en las respuestas GET
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Aquí hacemos la consulta de los tipos de usuario con detalles
        tipos_usuario_full = UsuarioTipoUsuario.objects.filter(usuario=instance)
        representation['tipos_usuario'] = [
            {
                'id': tu.tipo_usuario.id,
                'name': tu.tipo_usuario.name
            }
            for tu in tipos_usuario_full
        ]
        
        return representation
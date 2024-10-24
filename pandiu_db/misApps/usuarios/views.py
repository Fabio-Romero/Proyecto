from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from misApps.usuarios.models import Usuario, TipoUsuario, UsuarioTipoUsuario
from misApps.usuarios.serializers import UsuarioSerializer, TipoUsuarioSerializer, UsuarioTipoUsuarioSerializer

# Vistas para Usuario
class UsuarioList(APIView):
    """
    Lista todos los usuarios o crea uno nuevo.
    """
    def get(self, request, format=None):
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsuarioDetail(APIView):
    """
    Retrieve, update o delete de un usuario específico.
    """
    def get_object(self, pk):
        try:
            return Usuario.objects.get(pk=pk)
        except Usuario.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        usuario = self.get_object(pk)
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        usuario = self.get_object(pk)
        serializer = UsuarioSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        usuario = self.get_object(pk)
        serializer = UsuarioSerializer(usuario, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        usuario = self.get_object(pk)
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Vistas para TipoUsuario
class TipoUsuarioList(APIView):
    """
    Lista todos los tipos de usuario o crea uno nuevo.
    """
    def get(self, request, format=None):
        tipos = TipoUsuario.objects.all()
        serializer = TipoUsuarioSerializer(tipos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TipoUsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TipoUsuarioDetail(APIView):
    """
    Retrieve, update o delete de un tipo de usuario específico.
    """
    def get_object(self, pk):
        try:
            return TipoUsuario.objects.get(pk=pk)
        except TipoUsuario.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        tipo_usuario = self.get_object(pk)
        serializer = TipoUsuarioSerializer(tipo_usuario)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        tipo_usuario = self.get_object(pk)
        serializer = TipoUsuarioSerializer(tipo_usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        tipo_usuario = self.get_object(pk)
        tipo_usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Vistas para UsuarioTipoUsuario (relación Many-to-Many)
class UsuarioTipoUsuarioList(APIView):
    """
    Lista todos los UsuarioTipoUsuario o crea uno nuevo.
    """
    def get(self, request, format=None):
        usuario_tipos = UsuarioTipoUsuario.objects.all()
        serializer = UsuarioTipoUsuarioSerializer(usuario_tipos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UsuarioTipoUsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsuarioTipoUsuarioDetail(APIView):
    """
    Retrieve, update o delete de un UsuarioTipoUsuario específico.
    """
    def get_object(self, pk):
        try:
            return UsuarioTipoUsuario.objects.get(pk=pk)
        except UsuarioTipoUsuario.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        usuario_tipo = self.get_object(pk)
        serializer = UsuarioTipoUsuarioSerializer(usuario_tipo)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        usuario_tipo = self.get_object(pk)
        serializer = UsuarioTipoUsuarioSerializer(usuario_tipo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        usuario_tipo = self.get_object(pk)
        usuario_tipo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

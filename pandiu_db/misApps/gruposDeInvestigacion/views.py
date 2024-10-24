from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from misApps.gruposDeInvestigacion.models import GrupoInvestigacion
from misApps.gruposDeInvestigacion.serializers import GrupoInvestigacionSerializer

# Vista para listar todos los grupos de investigación
class GrupoInvestigacionList(APIView):
    """
    Lista todos los grupos de investigación o crea uno nuevo.
    """
    def get(self, request, format=None):
        grupos = GrupoInvestigacion.objects.all()
        serializer = GrupoInvestigacionSerializer(grupos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GrupoInvestigacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Vista para obtener, actualizar o eliminar un grupo de investigación específico
class GrupoInvestigacionDetail(APIView):
    """
    Retrieve, update o delete de un grupo de investigación específico.
    """
    def get_object(self, pk):
        try:
            return GrupoInvestigacion.objects.get(pk=pk)
        except GrupoInvestigacion.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        grupo = self.get_object(pk)
        serializer = GrupoInvestigacionSerializer(grupo)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        grupo = self.get_object(pk)
        serializer = GrupoInvestigacionSerializer(grupo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        grupo = self.get_object(pk)
        serializer = GrupoInvestigacionSerializer(grupo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        grupo = self.get_object(pk)
        grupo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


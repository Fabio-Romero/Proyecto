from django.urls import path
from misApps.gruposDeInvestigacion.views import GrupoInvestigacionList, GrupoInvestigacionDetail

app_name = "gruposDeInvestigacion"

urlpatterns = [
    # Ruta predeterminada para listar y detallar grupos de investigación
    path('', GrupoInvestigacionList.as_view(), name="grupo-investigacion-list"),
    path('<int:pk>/', GrupoInvestigacionDetail.as_view(), name="grupo-investigacion-detail"),
]

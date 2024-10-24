from django.urls import path
from misApps.facultades.views import FacultadList, FacultadDetail, ProgramaList, ProgramaDetail

app_name = "facultades"

urlpatterns = [
    # Ruta predeterminada para listar y detallar facultades
    path('', FacultadList.as_view(), name="facultad-list"),
    path('<int:pk>/', FacultadDetail.as_view(), name="facultad-detail"),
    
    # Rutas para programas
    path('programas/', ProgramaList.as_view(), name="programa-list"),
    path('programas/<int:pk>/', ProgramaDetail.as_view(), name="programa-detail"),
]

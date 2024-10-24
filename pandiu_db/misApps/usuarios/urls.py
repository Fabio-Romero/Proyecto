from django.urls import path
from misApps.usuarios.views import (
    UsuarioList, UsuarioDetail, 
    TipoUsuarioList, TipoUsuarioDetail, 
    UsuarioTipoUsuarioList, UsuarioTipoUsuarioDetail
)

app_name = "usuarios"

urlpatterns = [
    # Usuario List y Detail
    path('', UsuarioList.as_view(), name="usuario-list"),
    path('<int:pk>/', UsuarioDetail.as_view(), name="usuario-detail"),

    # TipoUsuario List y Detail
    path('tipos-usuario/', TipoUsuarioList.as_view(), name="tipousuario-list"),
    path('tipos-usuario/<int:pk>/', TipoUsuarioDetail.as_view(), name="tipousuario-detail"),

    # UsuarioTipoUsuario List y Detail
    path('usuario-tipos/', UsuarioTipoUsuarioList.as_view(), name="usuariotipousuario-list"),
    path('usuario-tipos/<int:pk>/', UsuarioTipoUsuarioDetail.as_view(), name="usuariotipousuario-detail"),
]

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from misApps.publicaciones.views import (
    PublicacionList, PublicacionDetail, 
    TipoPublicacionList, TipoPublicacionDetail,  
    PalabraClaveList, PalabraClaveDetail
)

app_name = "publicaciones"

urlpatterns = [
    # Publicacion List and Detail
    path('', PublicacionList.as_view(), name="publicacion-list"),
    path('<int:pk>/', PublicacionDetail.as_view(), name="publicacion-detail"),

    # TipoPublicacion List and Detail
    path('tipos-publicacion/', TipoPublicacionList.as_view(), name="tipopublicacion-list"),
    path('tipos-publicacion/<int:pk>/', TipoPublicacionDetail.as_view(), name="tipopublicacion-detail"),

    # PalabraClave List and Detail
    path('palabras-clave/', PalabraClaveList.as_view(), name="palabraclave-list"),
    path('palabras-clave/<int:pk>/', PalabraClaveDetail.as_view(), name="palabraclave-detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('apps.core.urls')),
    path('admin/', admin.site.urls),
    path('funcionarios/', include('apps.funcionarios.urls')),
    path('departamentos/', include('apps.departamentos.urls')),
    path('empresas/', include('apps.empresas.urls')),
    path('documentos/', include('apps.documentos.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

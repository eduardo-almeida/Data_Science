from django.urls import path
from .views import EmpresaCreate, EmpresaEdit

urlpatterns = [
    path('criarEmpresa', EmpresaCreate.as_view(), name='criarEmpresa'),
    path('editarEmpresa/<int:pk>', EmpresaEdit.as_view(), name='editarEmpresa'),
]
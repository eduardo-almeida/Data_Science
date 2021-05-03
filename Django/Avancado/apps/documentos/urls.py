from django.urls import path
from .views import DocumentoCreate#, DocumentoEdit

urlpatterns = [
    path('novo/<int:funcionario_id>/', DocumentoCreate.as_view(), name='criarDocumento'),
    #path('deletarDocumento/<int:pk>', DocumentoEdit.as_view(), name='deletarDocumento'),
]
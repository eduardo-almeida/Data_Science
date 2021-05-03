from django.urls import path
from .views import DepartamentosList, DepartamentosCreate, DepartamentosDelete, DepartamentosUpdate



urlpatterns = [
    path('list', DepartamentosList.as_view(), name='list_departamento'),
    path('novo/', DepartamentosCreate.as_view(), name='create_departamento'),
    path('delete/<int:pk>/', DepartamentosDelete.as_view(), name='delete_departamento'),
    path('update/<int:pk>/', DepartamentosUpdate.as_view(), name='update_departamento'),
]
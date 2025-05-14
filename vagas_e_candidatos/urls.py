from django.urls import path
from .views import index, vagas_index, candidatos_index

urlpatterns = [
    path('', index, name='dashboard'),
    path('vagas/', vagas_index, name='vagas_dashboard'),
    path('candidatos/', candidatos_index, name='candidatos_dashboard'),
]

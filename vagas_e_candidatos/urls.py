from django.urls import path
from .views import index, vagas_index, candidatos_index, dados_candidato_por_id

urlpatterns = [
    path('', index, name='dashboard'),
    path('vagas/', vagas_index, name='vagas_dashboard'),
    path('candidatos/', candidatos_index, name='candidatos_dashboard'),
    path(
        'candidatos/<parametro>',
        dados_candidato_por_id,
        name='dados_candidato_por_id'
    ),
]

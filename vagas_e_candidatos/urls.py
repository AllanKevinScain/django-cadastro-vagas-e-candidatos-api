from django.urls import path
from .views import index, vagas_index, candidatos_index, dados_candidato_por_id, dados_vaga_por_id, cadastrar_vaga

urlpatterns = [
    path('', index, name='dashboard'),
    path('vagas/', vagas_index, name='vagas_dashboard'),
    path('candidatos/', candidatos_index, name='candidatos_dashboard'),
    path(
        'candidatos/<parametro>',
        dados_candidato_por_id,
        name='dados_candidato_por_id'
    ),
    path(
        'vagas/<parametro>',
        dados_vaga_por_id,
        name='dados_vaga_por_id'
    ),
    path('cadastrar-vaga/', cadastrar_vaga, name='cadastrar_vaga'),
]

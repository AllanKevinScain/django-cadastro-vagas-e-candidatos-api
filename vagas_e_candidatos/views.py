from django.shortcuts import render
from .models import Vaga, Candidato


def index(request):
    return render(request, 'index.html')


def vagas_index(request):
    vagas = Vaga.objects.all()
    dados = {'vagas': vagas}

    return render(request, 'vagas/index.html', dados)


def candidatos_index(request):
    candidatos = Candidato.objects.all()
    dados = {'candidatos': candidatos}

    return render(request, 'candidatos/index.html', dados)


def dados_candidato_por_id(request, parametro):
    candidato = Candidato.objects.get(id=parametro)
    dados = {'candidato': candidato}

    return render(request, 'candidatos/candidato.html', dados)

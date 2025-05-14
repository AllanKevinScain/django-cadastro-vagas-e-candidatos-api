from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def vagas_index(request):
    return render(request, 'vagas/index.html')


def candidatos_index(request):
    return render(request, 'candidatos/index.html')

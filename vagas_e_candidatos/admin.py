from django.contrib import admin
from .models import Candidato, Vaga

@admin.register(Vaga)
class VagaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo')
    search_fields = ('titulo',)
    list_filter = ('titulo',)

@admin.register(Candidato)
class CandidatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'vaga')
    search_fields = ('nome',)
    list_filter = ('vaga',)

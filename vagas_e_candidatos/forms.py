from django import forms
from .models import Vaga, Candidato


class VagaForm(forms.ModelForm):
    class Meta:
        model = Vaga
        fields = ['titulo', 'area', 'tipo_contrato', 'descricao']


class CandidatoForm(forms.ModelForm):
    data_nascimento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Candidato
        fields = ['nome', 'sobrenome', 'data_nascimento',
                  'genero', 'email', 'telefone', 'escolaridade', 'vaga']

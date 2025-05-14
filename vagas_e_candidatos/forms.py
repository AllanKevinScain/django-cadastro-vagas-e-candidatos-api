from django import forms
from .models import Vaga


class VagaForm(forms.ModelForm):
    class Meta:
        model = Vaga
        fields = ['titulo', 'area', 'tipo_contrato', 'descricao']

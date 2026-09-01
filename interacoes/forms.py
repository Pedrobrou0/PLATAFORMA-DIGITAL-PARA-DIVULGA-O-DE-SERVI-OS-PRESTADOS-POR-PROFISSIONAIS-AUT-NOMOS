from django import forms
from .models import Solicitacao


class SolicitacaoForm(forms.ModelForm):

    class Meta:
        model = Solicitacao

        fields = [
            'cliente',
            'servico',
            'descricao'
        ]


class SolicitacaoEditarForm(forms.ModelForm):

    class Meta:
        model = Solicitacao

        fields = [
            'cliente',
            'servico',
            'descricao',
            'status'
        ]
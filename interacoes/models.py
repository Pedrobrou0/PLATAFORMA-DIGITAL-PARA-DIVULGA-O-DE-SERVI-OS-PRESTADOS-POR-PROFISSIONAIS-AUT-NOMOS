from django.db import models
from django.contrib.auth.models import User
from servicos.models import Servico


class StatusSolicitacao(models.TextChoices):
    PENDENTE = 'PENDENTE', 'Pendente'
    ACEITA = 'ACEITA', 'Aceita'
    RECUSADA = 'RECUSADA', 'Recusada'
    CANCELADA = 'CANCELADA', 'Cancelada'
    CONCLUIDA = 'CONCLUIDA', 'Concluída'


class Solicitacao(models.Model):
    cliente = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='solicitacoes'
    )

    servico = models.ForeignKey(
        Servico,
        on_delete=models.PROTECT,
        related_name='solicitacoes'
    )

    descricao = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=StatusSolicitacao.choices,
        default=StatusSolicitacao.PENDENTE
    )

    data_solicitacao = models.DateTimeField(
        auto_now_add=True
    )

    data_atualizacao = models.DateTimeField(
        auto_now=True
    )

    def aceitar(self):
        self.status = StatusSolicitacao.ACEITA
        self.save()

    def recusar(self):
        self.status = StatusSolicitacao.RECUSADA
        self.save()

    def cancelar(self):
        self.status = StatusSolicitacao.CANCELADA
        self.save()

    def concluir(self):
        self.status = StatusSolicitacao.CONCLUIDA
        self.save()

    def __str__(self):
        return f'{self.cliente} - {self.servico}'
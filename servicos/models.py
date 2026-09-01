from django.db import models
from usuarios.models import Profissional


class Categoria(models.Model):
    nome = models.CharField(
        max_length=100,
        unique=True
    )

    profissionais = models.ManyToManyField(
        Profissional,
        related_name='categorias',
        blank=True
    )

    def __str__(self):
        return self.nome


class Servico(models.Model):
    profissional = models.ForeignKey(
        Profissional,
        on_delete=models.CASCADE,
        related_name='servicos'
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name='servicos'
    )

    titulo = models.CharField(
        max_length=100
    )

    descricao = models.TextField()

    preco = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    imagem = models.ImageField(
        upload_to='servicos/',
        blank=True,
        null=True
    )

    data_cadastro = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.titulo
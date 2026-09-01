from django.db import models
from django.contrib.auth.models import User


class Profissional(User):
    telefone = models.CharField(max_length=20)
    cidade = models.CharField(max_length=100)
    descricao = models.TextField()

    foto = models.ImageField(
        upload_to='profissionais/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.get_full_name() or self.username
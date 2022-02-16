from mailbox import NotEmptyError
from django.db import models


class Igreja(models.Model):
    nome = models.CharField(max_length=30)
    profeta = models.CharField(max_length=30)
    numfieis = models.IntegerField()
    descricao = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

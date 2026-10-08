from django.db import models


class Politico(models.Model):
    nome = models.CharField(max_length=200)
    partido = models.CharField(max_length=20)
    uf = models.CharField(max_length=2)
    cargo = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
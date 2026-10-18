from django.db import models
import unicodedata


def remover_acentos(texto):
    if not texto:
        return ""
    nfkd = unicodedata.normalize('NFKD', texto)
    return "".join([c for c in nfkd if not unicodedata.combining(c)])

class Politico(models.Model):
    nome = models.CharField(max_length=100)
    nome_busca = models.CharField(max_length=100)
    partido = models.CharField(max_length=20)
    uf = models.CharField(max_length=2)
    cargo = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


    # Preenche os campos auxiliares sem acento antes de salvar
    def save(self, *args, **kwargs):
        self.nome_busca = remover_acentos(self.nome)
        super().save(*args, **kwargs)
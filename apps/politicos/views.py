from django.shortcuts import render
from django.db.models import Q
from .models import Politico
import unicodedata


def remover_acentos(texto):
    nfkd = unicodedata.normalize('NFKD', texto)
    return "".join([c for c in nfkd if not unicodedata.combining(c)])

def lista(request):
    termo = request.GET.get("q", "").strip()
    termo_busca = remover_acentos(termo)
    politicos = Politico.objects.all()

    if termo:
        politicos = politicos.filter(
            Q(nome_busca__contains=termo) | Q(partido__contains=termo)
        )

    return render(request, "politicos/lista.html", {
            "politicos": politicos,
            "termo": termo
    })
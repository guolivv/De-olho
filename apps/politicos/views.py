from django.shortcuts import render
from .models import Politico


def lista(request):
    politicos = Politico.objects.all()
    return render(request, "politicos/lista.html", {"politicos": politicos})
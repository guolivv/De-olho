import pytest
from django.urls import reverse
from apps.politicos.models import Politico


@pytest.fixture
def maria(db):
    return Politico.objects.create(
        nome="Maria Silva", partido="PT", uf="SP", cargo="Deputado Estadual"
    )


@pytest.fixture
def joao(db):
    return Politico.objects.create(
        nome="João Souza", partido="PL", uf="RJ", cargo="Senador"
    )


@pytest.fixture
def jose(db):
    return Politico.objects.create(
        nome="", partido="PT", uf="SP", cargo="Senador"
    )


@pytest.fixture
def get_lista(client):
    def _get(**params):
        return client.get(reverse("lista"), params)
    return _get
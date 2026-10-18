import pytest


def test_sem_termo_retorna_todos(get_lista, maria, joao):
    resp = get_lista()
    assert resp.status_code == 200
    assert set(resp.context["politicos"]) == {maria, joao}


@pytest.mark.parametrize("termo", ["maria", "MARIA", "silva", "PT"])
def test_busca_encontra_maria(get_lista, maria, joao, termo):
    resp = get_lista(q=termo)
    assert list(resp.context["politicos"]) == [maria]


def test_busca_por_partido(get_lista, maria, joao):
    resp = get_lista(q="PL")
    assert list(resp.context["politicos"]) == [joao]


def test_termo_com_espacos_e_ignorado(get_lista, maria, joao):
    resp = get_lista(q="   ")
    assert set(resp.context["politicos"]) == {maria, joao}


def test_sem_resultados_mostra_mensagem(get_lista, maria, joao):
    resp = get_lista(q="inexistente")
    assert list(resp.context["politicos"]) == []
    assert "Nenhum político encontrado" in resp.content.decode()


def test_objeto_sem_nome_retorna_vazio(get_lista, jose):
    resp = get_lista(q="")
    assert list(resp.context["politicos"]) == [jose]


def test_termo_volta_no_contexto(get_lista, maria):
    resp = get_lista(q="maria")
    assert resp.context["termo"] == "maria"


def test_busca_ignora_acentos(get_lista, joao):
    resp = get_lista(q="joao")
    assert list(resp.context["politicos"]) == [joao]
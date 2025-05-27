import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from agricultor.models import Agricultor

client = APIClient()

@pytest.mark.django_db
def test_filtrar_por_nome():

    Agricultor.objects.create(nome="Pedro", cpf="12345678901")
    Agricultor.objects.create(nome="Otavio", cpf="12345678902")

    url = reverse("agricultores-list")
    response = client.get(url, {"nome": "Pedro"})

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["nome"] == "Pedro"

@pytest.mark.django_db
def test_filtrar_por_cpf():

    Agricultor.objects.create(nome="Pedro", cpf="12345678901")
    Agricultor.objects.create(nome="Otavio", cpf="12345678902")

    url = reverse("agricultores-list")
    response = client.get(url, {"cpf": "12345678901"})

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["cpf"] == "12345678901"

@pytest.mark.django_db
def test_filtrar_por_telefone():

    Agricultor.objects.create(nome="Pedro", cpf="12345678901", telefone="54999998888")
    Agricultor.objects.create(nome="Otavio", cpf="12345678902", telefone="54999997777")

    client = APIClient()
    url = reverse("agricultores-list")
    response = client.get(url, {"telefone": "54999998888"})

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["telefone"] == "54999998888"

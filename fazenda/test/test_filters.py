import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from agricultor.models import Agricultor
from fazenda.models import Fazendas

client = APIClient()

@pytest.mark.django_db
def test_filtrar_por_nome():

    #Ciando 2 agricultores para poupar trabalho no teste
    agricultor1 = Agricultor.objects.create(nome="Pedro",cpf="12345678901",telefone="54999998888")
    agricultor2 = Agricultor.objects.create(nome="Otavio",cpf="12345678902",telefone="54999998888")


    fazenda = Fazendas.objects.create(
        nome="Fazenda Zwirtes",
        municipio="Vacaria",
        estado="RS",
        area_total="40",
        agricultor=agricultor1
    )

    fazenda = Fazendas.objects.create(
        nome="Fazenda Angelin",
        municipio="Vacaria",
        estado="RS",
        area_total="40",
        agricultor=agricultor2
    )

    url = reverse("fazendas-list")
    response = client.get(url, {"nome": "Fazenda Zwirtes"})

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["nome"] == "Fazenda Zwirtes"


@pytest.mark.django_db
def test_filtrar_por_municipio():

    #Ciando 2 agricultores para poupar trabalho no teste
    agricultor1 = Agricultor.objects.create(nome="Pedro",cpf="12345678901",telefone="54999998888")
    agricultor2 = Agricultor.objects.create(nome="Otavio",cpf="12345678902",telefone="54999998888")

    fazenda = Fazendas.objects.create(
        nome="Fazenda Zwirtes",
        municipio="Vacaria",
        estado="RS",
        area_total="40",
        agricultor=agricultor1
    )

    fazenda = Fazendas.objects.create(
        nome="Fazenda Angelin",
        municipio="Esmeralda",
        estado="RS",
        area_total="40",
        agricultor=agricultor2
    )

    url = reverse("fazendas-list")
    response = client.get(url, {"municipio": "Vacaria"})

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["municipio"] == "Vacaria"

@pytest.mark.django_db
def test_filtrar_por_estado():

    #Ciando 2 agricultores para poupar trabalho no teste
    agricultor1 = Agricultor.objects.create(nome="Pedro",cpf="12345678901",telefone="54999998888")
    agricultor2 = Agricultor.objects.create(nome="Otavio",cpf="12345678902",telefone="54999998888")

    fazenda = Fazendas.objects.create(
        nome="Fazenda Zwirtes",
        municipio="Vacaria",
        estado="RS",
        area_total="40",
        agricultor=agricultor1
    )

    fazenda = Fazendas.objects.create(
        nome="Fazenda Angelin",
        municipio="Esmeralda",
        estado="SP",
        area_total="40",
        agricultor=agricultor2
    )

    url = reverse("fazendas-list")
    response = client.get(url, {"estado": "SP"})

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["estado"] == "SP"
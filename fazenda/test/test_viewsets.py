import pytest
from rest_framework.test import APIClient
from rest_framework import status
from fazenda.models import Fazendas
from agricultor.models import Agricultor

client = APIClient()

@pytest.mark.django_db
def test_criar_fazenda_api():

    agricultor = Agricultor.objects.create(
        nome="Pedro",
        cpf="12345678901",
        telefone="54999998888",
    )

    fazenda = {
        "nome" : "Fazenda Zwirtes",
        "municipio" : "Vacaria",
        "estado" : "RS",
        "area_total" : "40",
        "agricultor" : agricultor.id
    }

    response = client.post("/api/fazendas/", fazenda, format='json')
    assert response.status_code == 201
    assert response.data["nome"] == "Fazenda Zwirtes"

@pytest.mark.django_db
def test_editar_fazenda_api():

    agricultor = Agricultor.objects.create(
        nome="Pedro",
        cpf="12345678901",
        telefone="54999998888",
    )

    fazenda = Fazendas.objects.create(
        nome="Fazenda Zwirtes",
        municipio="Vacaria",
        estado="RS",
        area_total="40",
        agricultor=agricultor
    )

    url = f"/api/fazendas/{fazenda.id}/"
    response = client.patch(url, {"nome": "Fazenda Zwirtes Editado"}, format="json")

    assert response.status_code == status.HTTP_200_OK
    assert response.data["nome"] == "Fazenda Zwirtes Editado"

@pytest.mark.django_db
def test_deletar_fazenda_api():

    agricultor = Agricultor.objects.create(
        nome="Pedro",
        cpf="12345678901",
        telefone="54999998888",
    )

    fazenda = Fazendas.objects.create(
        nome="Fazenda Zwirtes",
        municipio="Vacaria",
        estado="RS",
        area_total="40",
        agricultor=agricultor
    )

    url = f"/api/fazendas/{fazenda.id}/"
    response = client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Fazendas.objects.filter(id=fazenda.id).exists()

@pytest.mark.django_db
def test_fazenda_nao_encontrada_get():

    response = client.get("/api/fazendas/999/")
    assert response.status_code == status.HTTP_404_NOT_FOUND

@pytest.mark.django_db
def test_fazendas_nao_encontrada_delete():
    
    response = client.delete("/api/fazendas/999/")
    assert response.status_code == status.HTTP_404_NOT_FOUND
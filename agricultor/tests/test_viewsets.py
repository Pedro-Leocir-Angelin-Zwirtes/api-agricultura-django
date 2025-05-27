import pytest
from rest_framework.test import APIClient
from rest_framework import status
from agricultor.models import Agricultor

client = APIClient()

@pytest.mark.django_db
def test_criar_agricultor_api():

    data = {
        "nome": "Pedro",
        "cpf": "12345678901",
        "telefone": "54999998888"
    }
    response = client.post("/api/agricultores/", data)
    assert response.status_code == 201 # **201** Indica que foi criado no banco 
    assert response.data["nome"] == "Pedro"

@pytest.mark.django_db
def test_listar_agricultores_api():

    Agricultor.objects.create(
        nome="Pedro", 
        cpf="12345678901", 
        telefone="54999998888"
    )
    response = client.get("/api/agricultores/")
    assert response.status_code == 200
    assert len(response.data) >= 1

@pytest.mark.django_db
def test_editar_agricultor_patch():

    agricultor = Agricultor.objects.create(
        nome="Pedro",
        cpf="12345678901",
        telefone="54999998888",
        data_registro="2025-05-22"
    )

    url = f"/api/agricultores/{agricultor.id}/"
    response = client.patch(url, {"nome": "Pedro Editado"}, format="json")

    assert response.status_code == status.HTTP_200_OK
    assert response.data["nome"] == "Pedro Editado"

@pytest.mark.django_db
def test_deletar_agricultor():

    agricultor = Agricultor.objects.create(
        nome="Pedro",
        cpf="12345678901",
        telefone="54999998888",
        data_registro="2025-05-22"
    )

    url = f"/api/agricultores/{agricultor.id}/"
    response = client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Agricultor.objects.filter(id=agricultor.id).exists()

@pytest.mark.django_db
def test_cpf_duplicado():

    Agricultor.objects.create(
        nome="Pedro",
        cpf="12345678901",
        telefone="54999998888",
        data_registro="2025-05-22"
    )

    response = client.post("/api/agricultores/", {
        "nome": "Outro",
        "cpf": "12345678901",  # CPF duplicado
        "telefone": "54999998888",
        "data_registro": "2025-05-22"
    }, format="json")

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "cpf" in response.data

@pytest.mark.django_db
def test_nome_vazio():

    response = client.post("/api/agricultores/", {
        "nome": "",  # Nome vazio
        "cpf": "12345678901",
        "telefone": "54999998888",
        "data_registro": "2025-05-22"
    }, format="json")

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "nome" in response.data

@pytest.mark.django_db
def test_agricultor_nao_encontrado_get():

    response = client.get("/api/agricultores/999/")
    assert response.status_code == status.HTTP_404_NOT_FOUND

@pytest.mark.django_db
def test_agricultor_nao_encontrado_delete():
    
    response = client.delete("/api/agricultores/999/")
    assert response.status_code == status.HTTP_404_NOT_FOUND
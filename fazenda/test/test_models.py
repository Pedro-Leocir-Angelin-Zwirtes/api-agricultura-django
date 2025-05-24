import pytest
from fazenda.models import Fazendas
from agricultor.models import Agricultor
from django.core.exceptions import ValidationError
from django.db import IntegrityError

@pytest.mark.django_db
def test_criar_fazenda():

    agricultor = Agricultor.objects.create(
        nome="Pedro",
        cpf="12345678901",
        telefone="54999998888",
        #data_registro="2025-05-22",
    )

    fazenda = Fazendas.objects.create(
        nome="Fazenda Zwirtes",
        municipio="Vacaria",
        estado="RS",
        area_total="40",
        agricultor=agricultor
    )

    assert fazenda.nome == "Fazenda Zwirtes"
    assert fazenda.municipio == "Vacaria"
    assert fazenda.estado == "RS"
    assert fazenda.area_total == "40"
    assert fazenda.agricultor.nome == "Pedro"

@pytest.mark.django_db
def test_testando_tamanho_dos_campos():

    agricultor = Agricultor.objects.create(
        nome="Pedro" * 101,
        cpf="12345678901" * 2,
        telefone="54999998888" * 12,
        #data_registro="2025-05-22",
    )

    fazenda = Fazendas.objects.create(
        nome="Fazenda Zwirtes" * 268,
        municipio="Vacaria" * 268,
        estado="RS" * 268,
        area_total="40" * 268,
        agricultor=agricultor
    )
    with pytest.raises(ValidationError):
        fazenda.full_clean()

@pytest.mark.django_db
def test_retornar_nome_fazenda():

    agricultor = Agricultor.objects.create(
        nome="Pedro",
        cpf="12345678901",
        telefone="54999998888",
        #data_registro="2025-05-22",
    )

    fazenda = Fazendas.objects.create(
        nome="Fazenda Zwirtes",
        municipio="Vacaria",
        estado="RS",
        area_total="40",
        agricultor=agricultor
    )
    
    assert str(fazenda) == "Fazenda Zwirtes"

@pytest.mark.django_db
def test_retornar_nome_fazenda_obrigatorio():

    agricultor = Agricultor.objects.create(
        nome="Pedro",
        cpf="12345678901",
        telefone="54999998888",
        #data_registro="2025-05-22",
    )

    fazenda = Fazendas.objects.create(
        nome="",
        municipio="Vacaria",
        estado="RS",
        area_total="40",
        agricultor=agricultor
    )
    
    with pytest.raises(ValidationError):
        fazenda.full_clean()
import pytest
from agricultor.models import Agricultor
from django.core.exceptions import ValidationError
from django.db import IntegrityError

@pytest.mark.django_db
def test_criar_agricultor():

    agricultor = Agricultor.objects.create(
        nome="Pedro",
        cpf="12345678901",
        telefone="54999998888",
        #data_registro="2025-05-22",
    )

    assert agricultor.nome == "Pedro"
    assert agricultor.cpf == "12345678901"
    assert agricultor.telefone == "54999998888"
    #assert str(agricultor.data_registro) == "2025-05-22"
    #Como está com auto_now_add não precisa testar o django preenche automaticamente

@pytest.mark.django_db
def test_testando_tamanho_dos_campos():

    agricultor = Agricultor(
        nome="Pedro" * 101,
        cpf="12345678901" * 2,
        telefone="54999998888" * 12,
    )
    with pytest.raises(ValidationError):
        agricultor.full_clean()

@pytest.mark.django_db
def test_cpf_unico():

    Agricultor.objects.create(
        nome="Pedro",
        cpf="1234567890",
        telefone="54999998888",
    )

    with pytest.raises(IntegrityError): # Pode ser Exception que serve para qualquer tipo de erro
        Agricultor.objects.create(
            nome="Jadir",
            cpf="1234567890",
            telefone="54999998888",
        )

@pytest.mark.django_db
def test_data_registro_auto():

    agricultor = Agricultor.objects.create(
        nome="Pedro",
        cpf="12345678901",
        telefone="54999998888"
    )
    assert agricultor.data_registro is not None

@pytest.mark.django_db
def test_retornar_nome():

    agriculor =Agricultor.objects.create(
        nome="Pedro",
        cpf="12345678901",
        telefone="54999998888"
    )

    assert str(agriculor) == "Pedro"

@pytest.mark.django_db
def test_nome_obrigatorio():
    
    agricultor = Agricultor(
        nome="",
        cpf="12345678901",
        telefone="54912345678"
    )
    with pytest.raises(ValidationError):
        agricultor.full_clean()
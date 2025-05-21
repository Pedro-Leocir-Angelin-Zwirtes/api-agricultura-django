from django.db import models
from talhao.models import Talhao

class AtividadesAgricola(models.Model):

    tipo = models.CharField(max_length=255)
    produto_utilizado = models.CharField(max_length=255)
    quantidade = models.IntegerField()
    operador = models.CharField(max_length=100)
    observacoes = models.TextField(max_length=255)
    data_execusao = models.DateField()
    talhao_nome = models.ForeignKey(Talhao, related_name="AtividadesAgricola", on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
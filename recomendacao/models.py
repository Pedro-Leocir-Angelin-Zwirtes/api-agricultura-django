from django.db import models
from talhao.models import Talhao

class Recomdacoes(models.Model):

    tipo = models.CharField(max_length=255)
    descricao = models.TextField(max_length=255)
    geracao = models.DateField(auto_now_add=True)
    talhao_recomendacao = models.ForeignKey(Talhao, related_name="Recomendacoes", on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

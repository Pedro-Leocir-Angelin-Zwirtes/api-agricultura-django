from django.db import models
from agricultor.models import Agricultor

class Fazendas(models.Model):

    nome = models.CharField(max_length=255)
    municipio = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    area_total = models.FloatField(max_length=255)
    agricultor = models.ForeignKey(Agricultor, related_name="fazendas", on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
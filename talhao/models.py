from django.db import models
from fazenda.models import Fazendas

class Talhao(models.Model):

    CULTURA_ATUAL = {
        "Soja": "Soja",
        "Milho": "Milho",
        "Feijão": "Feijão",
        "Arroz": "Arroz",
        "Trigo": "Trigo",
        "Cevada": "Cevada",
        "Algodão": "Algodão",
        "Girassol": "Girassol",
        
        "Café": "Café",
        "Cana-de-açúcar": "Cana-de-açúcar",
        "Laranja": "Laranja",
        "Limão": "Limão",
        "Uva": "Uva",
        "Abacate": "Abacate",
        "Açaí": "Açaí",
        "Coco": "Coco",
        
        "Tomate": "Tomate",
        "Alface": "Alface",
        "Cenoura": "Cenoura",
        "Cebola": "Cebola",
        "Batata": "Batata",
        "Pimentão": "Pimentão",
        
        "Agrofloresta": "Agrofloresta",
    }

    nome = models.CharField(max_length=100)
    cultura_atual = models.CharField(choices=CULTURA_ATUAL, max_length=255)
    area = models.CharField(max_length=100)
    data_plantio = models.DateField()
    fazenda = models.ForeignKey(Fazendas, related_name="talhao", on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nome} ({self.fazenda.nome})"
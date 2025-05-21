from rest_framework import serializers
from atividadeAgricola import models
from talhao.models import Talhao

class AatividadesAgricolaSerializers(serializers.ModelSerializer):
    nome_talhao = serializers.SerializerMethodField()

    class Meta:
        model = models.AtividadesAgricola
        fields = [
            'tipo',
            'produto_utilizado',
            'quantidade',
            'operador',
            'observacoes',
            'data_execusao',
            'talhao_nome',
            'nome_talhao',
        ]

    def get_nome_talhao(self, obj):
        return obj.talhao_nome.nome if obj.talhao_nome else None
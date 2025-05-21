from rest_framework import serializers
from recomendacao import models
from talhao.models import Talhao

class RecomedacoesSerializers(serializers.ModelSerializer):
    nome_talhao = serializers.SerializerMethodField()

    class Meta:
        model = models.Recomdacoes
        fields = [
            'tipo',
            'descricao',
            'geracao',
            'talhao_recomendacao',
            'nome_talhao'
        ]

    def get_nome_talhao(self, obj):
        return obj.talhao_recomendacao.nome if obj.talhao_recomendacao else None


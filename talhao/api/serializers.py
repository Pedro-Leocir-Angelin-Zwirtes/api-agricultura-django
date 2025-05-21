from rest_framework import serializers
from talhao import models

class TalhoesSerializers(serializers.ModelSerializer):
    nome_fazenda = serializers.SerializerMethodField()

    class Meta:
        model = models.Talhao
        fields = [
            'nome',
            'cultura_atual',
            'area',
            'data_plantio',
            'fazenda',
            'nome_fazenda'
        ]

    def get_nome_fazenda(self, obj):
        return obj.fazenda.nome if obj.fazenda else None
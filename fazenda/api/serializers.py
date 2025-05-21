from rest_framework import serializers
from fazenda import models
from agricultor.models import Agricultor

class FazendasSerliaziers(serializers.ModelSerializer):
    nome_agricultor = serializers.SerializerMethodField()
    
    class Meta:
        model = models.Fazendas
        fields = [
            'nome',
            'municipio',
            'estado',
            'area_total',
            'agricultor',
            'nome_agricultor',
        ]

    def get_nome_agricultor(self, obj):
        return obj.agricultor.nome if obj.agricultor else None
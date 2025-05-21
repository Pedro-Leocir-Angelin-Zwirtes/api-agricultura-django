from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from recomendacao.api import serializers
from recomendacao import models
from recomendacao.api.filters import RecomendacaoFilter

class RecomendacoesViewSets(viewsets.ModelViewSet):

    serializer_class = serializers.RecomedacoesSerializers
    queryset = models.Recomdacoes.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = RecomendacaoFilter  
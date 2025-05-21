from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from atividadeAgricola.api import serializers
from atividadeAgricola import models
from atividadeAgricola.api.filters import AtividadesAgricolaFilter

class AtividadesAgricolasViewSets(viewsets.ModelViewSet):

    serializer_class = serializers.AatividadesAgricolaSerializers
    queryset = models.AtividadesAgricola.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = AtividadesAgricolaFilter
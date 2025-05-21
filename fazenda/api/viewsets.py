from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from fazenda.api import serializers
from fazenda import models
from fazenda.api.filters import FazendaFilter

class FazendasViewSets(viewsets.ModelViewSet):
    
    serializer_class = serializers.FazendasSerliaziers
    queryset = models.Fazendas.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = FazendaFilter
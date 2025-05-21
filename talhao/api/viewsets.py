from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from talhao.api import serializers
from talhao import models
from talhao.api.filters import TalhaoFilter

class TalhoesViewSets(viewsets.ModelViewSet):

    serializer_class = serializers.TalhoesSerializers
    queryset = models.Talhao.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = TalhaoFilter
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from agricultor.api import serializers
from agricultor import models
from agricultor.api.filters import AgricultorFilter

class AgricultorViewSets(viewsets.ModelViewSet):

    serializer_class = serializers.AgricultorSerializers
    queryset = models.Agricultor.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = AgricultorFilter
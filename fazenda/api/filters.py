import django_filters
from fazenda import models

class FazendaFilter(django_filters.FilterSet):

    nome = django_filters.CharFilter(lookup_expr='icontains')
    municipio = django_filters.CharFilter(lookup_expr='icontains')
    estado = django_filters.CharFilter(lookup_expr='icontains')
    #area_total = django_filters.NumberFilter(lookup_expr='gte')

    class Meta:
        model = models.Fazendas
        fields = ['nome', 'municipio', 'estado']
import django_filters
from talhao import models

class TalhaoFilter(django_filters.FilterSet):

    nome = django_filters.CharFilter(lookup_expr='icontains')
    cultura_atual = django_filters.CharFilter(lookup_expr='icontains')
    data_plantio = django_filters.DateFilter(field_name="data_plantio")
    fazenda = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:

        model = models.Talhao
        fields = ['nome','cultura_atual', 'data_plantio', 'fazenda']

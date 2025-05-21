import django_filters
from atividadeAgricola import models

class AtividadesAgricolaFilter(django_filters.FilterSet):

    tipo = django_filters.CharFilter(lookup_expr='icontains')
    produto_utilizado = django_filters.CharFilter(lookup_expr='icontains')
    operador = django_filters.CharFilter(lookup_expr='icontains')
    data_execusao = django_filters.DateFilter(field_name="data_execusao")
    talhao_nome = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = models.AtividadesAgricola
        fields = ['tipo', 'produto_utilizado', 'operador', 'data_execusao', 'talhao_nome']
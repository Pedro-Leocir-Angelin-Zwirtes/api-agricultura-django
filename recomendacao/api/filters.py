import django_filters
from recomendacao import models

class RecomendacaoFilter(django_filters.FilterSet):

    tipo = django_filters.CharFilter(lookup_expr='icontains')
    descricao = django_filters.CharFilter(lookup_expr='icontains')
    talhao = django_filters.CharFilter(field_name='talhao_recomendacao__nome', lookup_expr='icontains')

    class Meta:

        model = models.Recomdacoes
        fields = ['tipo','descricao','talhao']
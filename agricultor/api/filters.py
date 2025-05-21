import django_filters
from agricultor import models

class AgricultorFilter(django_filters.FilterSet):

    nome = tipo = django_filters.CharFilter(lookup_expr='icontains')
    cpf = tipo = django_filters.CharFilter(lookup_expr='icontains')
    telefone = tipo = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = models.Agricultor
        fields = ['nome', 'cpf', 'telefone']
import django_filters
from agricultor import models

class AgricultorFilter(django_filters.FilterSet):

    nome = django_filters.CharFilter(lookup_expr='icontains')
    cpf = django_filters.CharFilter(lookup_expr='icontains')
    telefone = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = models.Agricultor
        fields = ['nome', 'cpf', 'telefone']
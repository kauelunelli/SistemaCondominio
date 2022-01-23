from sqlite3 import Date
from django.forms import BooleanField
from django_filters import DateFilter, CharFilter, ChoiceFilter
from django.utils.timezone import now
import django_filters

from .models import Despesa



class DespesaFilter(django_filters.FilterSet):
    dataVencimento = DateFilter(field_name="vencimento_fatura", lookup_expr='lte')
    unidade = CharFilter(field_name='unidade', lookup_expr='icontains')

    class Meta:
        model = Despesa
        fields = '__all__'
        exclude = ['unidade', 'vencimento_fatura']

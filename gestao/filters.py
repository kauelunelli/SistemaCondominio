from django_filters import DateFilter
import django_filters

from .models import Despesa

class DespesaFilter(django_filters.FilterSet):
    class Meta:
        model = Despesa
        fields = '__all__'


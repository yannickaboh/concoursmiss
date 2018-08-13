import django_filters
from .models import Gprovince


class GprovinceFilter(django_filters.FilterSet):
	nom = django_filters.CharFilter(lookup_expr='icontains')
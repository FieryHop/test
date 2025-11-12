from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.core.cache import cache
from rest_framework.response import Response
from django.db import models
import django_filters

from .models import Item
from .serializers import ItemSerializer


class ItemFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    category = django_filters.CharFilter(field_name='category', lookup_expr='iexact')

    class Meta:
        model = Item
        fields = ['category', 'price_min', 'price_max']


class ItemListView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = ItemFilter  # подключаем свой фильтр
    search_fields = ['name']
    pagination_class = None


class AvgPriceByCategoryView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        cache_key = 'avg_price_by_category'
        result = cache.get(cache_key)
        if result is None:
            qs = Item.objects.values('category').annotate(avg_price=models.Avg('price'))
            result = list(qs)
            cache.set(cache_key, result, 300)
        return Response(result)


# Create your views here.

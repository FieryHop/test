from django.urls import path
from .views import ItemListView, AvgPriceByCategoryView

urlpatterns = [
    path('items/', ItemListView.as_view()),
    path('stats/avg-price-by-category/', AvgPriceByCategoryView.as_view()),
]
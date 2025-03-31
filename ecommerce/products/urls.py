from django.urls import path
from .views import products_view, add_product

urlpatterns = [
    path('', products_view, name='products'),
    path('category/<int:category_id>/', products_view, name='category_products'),
    path('add/', add_product, name='add_product'),
]

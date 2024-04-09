from django.urls import path
from . import views

urlpatterns = [
    
    path('products',views.products , name='products_page'),
    path('product',views.product , name='product_page'),
    path('search',views.search , name='search_page'),
]
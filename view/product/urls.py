from django.urls import path

from product.views import ProductListView, ProductListAPI

app_name = 'product'

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('<int:page>/', ProductListAPI.as_view(), name='product-api')
]















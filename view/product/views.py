from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Product


class ProductListView(View):
    def get(self, request):
        return render(request, 'task/product/product.html')


class ProductListAPI(APIView):
    def get(self, request, page):
        row_count = 5

        offset = (page - 1) * row_count
        limit = page * row_count

        columns = [
            'id',
            'product_name',
            'product_price',
            'product_stock',
        ]
        products = Product.enabled_objects.values(*columns)[offset:limit]

        has_next = Product.enabled_objects.filter()[limit:limit + 1].exists()

        product_info = {
            'products': products,
            'hasNext': has_next
        }
        return Response(product_info)



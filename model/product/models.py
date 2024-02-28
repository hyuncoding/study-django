from django.db import models

from model.models import Period
from product.managers import ProductManager


class Product(Period):
    product_name = models.TextField(null=False, blank=False)
    product_price = models.BigIntegerField(null=False, blank=False)
    product_discount = models.SmallIntegerField(null=False, blank=False, default=0)
    # 판매중, 판매 중지
    status = models.BooleanField(null=False, default=False)
    objects = models.Manager()
    sell_price_objects = ProductManager()

    class Meta:
        db_table = 'tbl_product'
        # 다른 객체에서 참조로 Product에 접근할 때 사용할 manager 설정
        base_manager_name = 'sell_price_objects'
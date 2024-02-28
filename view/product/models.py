from django.db import models

from product.managers import ProductManager


class Product(models.Model):
    product_name = models.CharField(max_length=20, null=False, blank=False)
    product_price = models.IntegerField(null=False, default=0)
    product_stock = models.IntegerField(null=False, default=0)
    product_status = models.BooleanField(null=False, default=True)

    objects = models.Manager()
    enabled_objects = ProductManager()

    class Meta:
        db_table = 'tbl_product'
        ordering = ['-id']

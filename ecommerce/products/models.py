from django.db import models
from django.utils.translation import gettext_lazy as _

from products import enums
# from core import BaseAbstractModel

class Product(models.Model):
    # id otomatik oluşturulacaktır. bu yüzden bu sütun için bişi tanımlamaya gerek yok.
    # sadece custom bi id yapılacak ise override edilir.

    sku = models.CharField(
        max_length=100,
        verbose_name=_("SKU"),
    )
    name = models.CharField(
        max_length=255,
        verbose_name=_("Name"),
    )
    description = models.TextField(
        max_length=2000,
        verbose_name=_("Description"),
    )
    color = models.CharField(
        max_length=20,
        choices=enums.Colors.choices,
        verbose_name=_("Color"),
    )
    size = models.CharField(
        max_length=10,
        verbose_name=_("Size")
    )

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")

    def __str__(self):
        return self.sku

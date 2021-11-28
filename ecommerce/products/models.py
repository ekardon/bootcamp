from django.db import models
from django.utils.translation import gettext_lazy as _

from products import enums
from core import models as core_models


class Product(core_models.BaseAbstractModel):
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
        return f"{self.sku} - {self.name}"


class Stock(core_models.BaseAbstractModel):
    product = models.OneToOneField(
        to=Product,
        verbose_name=_("Product"),
        on_delete=models.PROTECT,
    )
    quantity = models.PositiveIntegerField(
        verbose_name=_("Quantity"),
    )

    class Meta:
        verbose_name = _("stock")
        verbose_name_plural = _("stocks")

    def __str__(self):
        return f"{self.product} - {self.quantity}"


class Price(core_models.BaseAbstractModel):
    product = models.OneToOneField(
        to=Product,
        verbose_name=_("Product"),
        on_delete=models.PROTECT,
    )
    amount = models.DecimalField(
        verbose_name=_("Amount"),
        max_digits=10,
        decimal_places=2,
    )

    class Meta:
        verbose_name = _("price")
        verbose_name_plural = _("prices")

    def __str__(self):
        return f"{self.product} - {self.amount}"



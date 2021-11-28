from django.contrib import admin

from products.models import Product, Stock, Price


class StockInline(admin.StackedInline):
    model = Stock


class PriceInline(admin.StackedInline):
    model = Price


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ("name", "sku")
    list_display = ("sku", "name", "color", "size")
    inlines = [StockInline, PriceInline]


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    search_fields = ("product__name", )
    list_display = ("product", "quantity")
    autocomplete_fields = ("product", )


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    search_fields = ("product__name", "product__sku")
    list_display = ("product", "amount")
    autocomplete_fields = ("product", )


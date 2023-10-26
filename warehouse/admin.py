from django.contrib import admin

from warehouse.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ("id", "created_at")

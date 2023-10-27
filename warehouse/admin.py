from django.contrib import admin

from warehouse.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ("id", "created_at")
    list_display = ("id", "name", "price", "author", "created_at")
    list_filter = ("author", "created_at")
    search_fields = ("name", "author__username")

from django.urls import path

from warehouse.views import ProductViewSet

product_list = ProductViewSet.as_view(
    actions={
        "get": "list",
        "post": "create",
    }
)
product_detail = ProductViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

urlpatterns = [
    path("products/", product_list, name="product-list"),
    path("products/<int:pk>/", product_detail, name="product-detail"),
]

app_name = "warehouse"

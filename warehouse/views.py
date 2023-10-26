from rest_framework import viewsets

from warehouse.models import Product
from warehouse.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from comprame.apps.compras.mixins import DefaultViewSetMixin, ModelViewSetMixin
from comprame.apps.compras.models import Product, Client, Purchase, PurchaseItem
from comprame.apps.compras.serializers import \
    ProductSerializer, ClientSerializer, PurchaseSerializer, \
    PurchaseItemSerializer


class ProductViewSet(DefaultViewSetMixin, ModelViewSetMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields =('title', 'price', 'tags')
    ordering_fields = ('title', 'price', 'tags')


class ClientViewSet(DefaultViewSetMixin, ModelViewSetMixin):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    search_fields = ('email', )


class PurchaseViewSet(DefaultViewSetMixin, ModelViewSetMixin):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


class PurchaseItemViewSet(DefaultViewSetMixin, ModelViewSet):
    queryset = PurchaseItem.objects.all()
    serializer_class = PurchaseItemSerializer



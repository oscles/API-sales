from rest_framework import serializers

from comprame.apps.compras.models import Client, Product, Purchase, PurchaseItem


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'email', 'details',)


class PurchaseItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.title')

    class Meta:
        model = PurchaseItem
        fields = ('id', 'purchase', 'product', 'product_name',
                  'price', 'quantity', 'state', )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'tags',)


class PurchaseSerializer(serializers.ModelSerializer):
    created = serializers.SerializerMethodField()
    client = ClientSerializer()
    products = serializers.SerializerMethodField()
    # total = serializers.ReadOnlyField(source='get_total')
    
    def get_created(self, obj):
        format = obj.created_at.strftime('%A %d. %B %Y %I')
        return format

    def get_products(self, obj):
        items = PurchaseItem.objects.filter(purchase=obj)
        serializer = PurchaseItemSerializer(data=items, many=True)
        serializer.is_valid()
        return serializer.data
    
    class Meta:
        model = Purchase
        fields = ('id', 'client', 'products', 'name',
                  'address', 'state', 'zip_code', 'created', )

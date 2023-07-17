from rest_framework import serializers
from .models import Purchase, PurchaseItem
from product.serializers import ProductSerializer

class PurchaseItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = PurchaseItem
        fields = ['product', 'quantity']

class PurchaseSerializer(serializers.ModelSerializer):
    products = PurchaseItemSerializer(many=True)

    class Meta:
        model = Purchase
        fields = ['purchase_no', 'products', 'customer', 'total_price', 'purchase_date']

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        purchase = Purchase.objects.create(**validated_data)
        for product_data in products_data:
            PurchaseItem.objects.create(purchase=purchase, **product_data)
        return purchase

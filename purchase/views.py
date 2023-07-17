from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Purchase, PurchaseItem
from .serializers import PurchaseSerializer
from product.models import Product
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from .permissions import IsCustomer

class PurchaseListView(APIView):
    permission_classes = [IsAuthenticated, IsCustomer]

    def get(self, request):
        purchases = Purchase.objects.filter(customer=request.user)
        serializer = PurchaseSerializer(purchases, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PurchaseCreateView(APIView):
    permission_classes = [IsAuthenticated, IsCustomer]

    def post(self, request):
        serializer = PurchaseSerializer(data=request.data)
        if serializer.is_valid():
            products_data = serializer.validated_data.pop('products')

            # Check if the customer is trying to purchase more quantity than available for a product
            for product_data in products_data:
                product = product_data['product']
                quantity = product_data['quantity']
                if quantity > product.quantity:
                    return Response({'error': f"Cannot purchase more quantity than available for product '{product.name}'"},
                                    status=status.HTTP_400_BAD_REQUEST)

            # Create the purchase and purchase items
            purchase = serializer.save(customer=request.user)
            for product_data in products_data:
                product = product_data['product']
                quantity = product_data['quantity']
                PurchaseItem.objects.create(purchase=purchase, product=product, quantity=quantity)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

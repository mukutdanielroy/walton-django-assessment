from django.db import models
from authentication.models import CustomUser
from product.models import Product

class Purchase(models.Model):
    purchase_no = models.CharField(max_length=255)
    products = models.ManyToManyField(Product, through='PurchaseItem')
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateTimeField(auto_now_add=True)

class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

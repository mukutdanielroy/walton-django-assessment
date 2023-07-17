from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    specification = models.TextField()
    color = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=False)

    def __str__(self):
        return self.name

from django.db import models
from apps.orders.models import Order  

# Create your models here.

class Payment(models.Model):
     STATUS_CHOICES = [
    ("Active", "Active"),
    ("Inactive", "Inactive"),
]

     id = models.IntegerField(primary_key=True)
     order = models.OneToOneField(Order, on_delete=models.CASCADE)
     amount = models.DecimalField(max_digits=5, decimal_places=2)
     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Active")
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     def __str__(self):
          return f"{self.id} | {self.status}"


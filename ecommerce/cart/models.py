from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.utils.timezone import now

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchased_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.user.username} - {self.product.name} - {self.quantity} - {self.purchased_at}"


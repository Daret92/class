from django.db import models
from django.contrib.auth.models import User
from product.models import Product
class carUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    is_pendient = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class productsCarUser(models.Model):
    carUser = models.ForeignKey(carUser, on_delete=models.CASCADE, null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
    total = models.DecimalField(max_digits=4,decimal_places=3)


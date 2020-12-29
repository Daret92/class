from django.db import models
from django.contrib.auth.models import User

def name_of_image_product(instance,filename):
    return 'products/{0}/{1}'.format(instance.name,filename)
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name+" / "+self.description

class SubCategory(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=False,blank=False)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name+" / "+str(int(self.is_active))

class Product(models.Model):
    category = models.ForeignKey(SubCategory,on_delete=models.CASCADE,null=False,blank=False)
    name = models.CharField(max_length=50)
    barcode = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.FileField(upload_to=name_of_image_product)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class ProductInventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
    stock = models.DecimalField(max_digits=10, decimal_places=3)
    maxProduct = models.IntegerField()
    minProduct = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.product.name + ", Stock: " +str(self.stock)

class OrderHeaderUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    TotalOrder = models.DecimalField(max_digits=10,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrderBodyUser(models.Model):
    header = models.ForeignKey(OrderHeaderUser, on_delete=models.CASCADE, null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
    total = models.DecimalField(max_digits=10,decimal_places=3)
    
from django.contrib import admin
from product.models import Category,Product,SubCategory,ProductInventory
from product.forms import ProductForm
from users.models import carUser,productsCarUser,CustomUserProveedor
from django.utils.crypto import get_random_string
# Register your models here.

class SubCategoriaInline(admin.TabularInline):
    model = SubCategory
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubCategoriaInline,]
    
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    form = ProductForm

class AddTokenGenerator(admin.ModelAdmin):
    actions=[]


admin.site.register(CustomUserProveedor)
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductInventory)
admin.site.register(carUser)
admin.site.register(productsCarUser)

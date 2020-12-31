from django.contrib import admin
from product.models import Category,Product,SubCategory,ProductInventory
from product.forms import ProductForm
from users.models import carUser,productsCarUser
# Register your models here.

class SubCategoriaInline(admin.TabularInline):
    model = SubCategory
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubCategoriaInline,]
    
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    form = ProductForm

admin.site.register(Product,ProductAdmin)
admin.site.register(ProductInventory)
admin.site.register(carUser)
admin.site.register(productsCarUser)

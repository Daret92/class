from django.contrib import admin
from product.models import Category,Product,SubCategory
from product.forms import ProductForm
# Register your models here.

class SubCategoriaInline(admin.TabularInline):
    model = SubCategory
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubCategoriaInline,]
    
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product)

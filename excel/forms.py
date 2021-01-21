from django import forms
from product.models import Product,ProductXls

class UploadProductForm(forms.ModelForm):
    class Meta:
        model = ProductXls
        exclude = ('created_at','updated_at','user','is_upload')
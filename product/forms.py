from django import forms
from product.models import Product,ProductXls

class ProductForm(forms.ModelForm):
    def __init__(self, *args,**kwargs):
        super(ProductForm,self).__init__(*args, **kwargs)
        for item in self.fields:
            if item != "image":
                self.fields[item].widget.attrs['class'] = 'form-control'
    class Meta:
        model = Product
        exclude = ('created_at','updated_at')


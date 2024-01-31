from django.forms import forms, ModelForm, CharField, TextInput, Textarea, BooleanField, CheckboxInput, FileInput

from product.models import *


class VariantForm(ModelForm):
    class Meta:
        model = Variant
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
            'active': CheckboxInput(attrs={'class': 'form-check-input', 'id': 'active'})
        }


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name'}),
            'sku': TextInput(attrs={'class': 'form-control', 'placeholder': 'Product SKU'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Product Description'}),
        }


class ProductImageForm(ModelForm):
    class Meta:
        model = ProductImage
        fields = ['file_path']

        widgets = {
            'file_path': FileInput(attrs={'class': 'form-control'}),
        }

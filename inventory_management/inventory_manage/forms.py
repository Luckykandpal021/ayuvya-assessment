from django import forms
from .models import Product, ProductImage, Stock, Order

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_description', 'product_original_price', 'product_discounted_price']

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']


class StockForm(forms.ModelForm):
    class Meta:
        model=Stock
        fields=['quantity']

class OrderForm(forms.ModelForm):
    class Meta:
        model= Order
        fields=['quantity','order_source']
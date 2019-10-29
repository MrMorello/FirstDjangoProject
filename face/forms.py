from django.forms import ModelForm
from face.models import Order, Products


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['date', 'subdivision', 'reason', 'where']
        exclude = ['']


class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'price', 'quantity', 'measurement']
        exclude = ['']

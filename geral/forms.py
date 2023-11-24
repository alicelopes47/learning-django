# forms.py
from django import forms
from .models import produto

class ProductForm(forms.ModelForm):
    class Meta:
        model = produto
        fields = ['nome', 'preco', 'quantidade']
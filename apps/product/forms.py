from django import forms
from django.forms import modelformset_factory

from apps.product.models import Product, ReviewProduct


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class CreateReviewProductForm(forms.ModelForm):

    class Meta:
        model = ReviewProduct
        fields = ['body', 'user', 'product',]


# from django import forms
from rest_framework import serializers
from .models import Products

# class ProductForm(forms.ModelForm):
#     class Meta:
#         model=Products
#         fields=[
#             'title',
#             'content',
#             'price'
#         ]
        

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields=[
            'title',
            'content',
            'price',
            'sale_price'
        ]
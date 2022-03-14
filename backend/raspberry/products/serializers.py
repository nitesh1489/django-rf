from rest_framework import serializers
from .models import Products

class ProductSerializer(serializers.ModelSerializer):
    my_discount=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Products 
        fields=[
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]
    def get_my_discount(self,obj):
        
        try:
            print(obj.id)
            return obj.get_discount()
        except:
            return None
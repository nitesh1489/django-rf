from django.db import models

# Create your models here.
class Products(models.Model):
    title=models.CharField(max_length=100)
    price=models.DecimalField(decimal_places=2,max_digits=10,default=99.99)
    content=models.TextField(null=True,blank=True)
    
    @property
    def sale_price(self):
        return  "%.2f" %(float(self.price)*0.8)

    def get_discount(self):
        return '12.2'
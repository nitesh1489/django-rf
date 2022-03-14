from attr import fields
from django.http import JsonResponse
from products.models import Products
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer
'''
@api_view(['GET','POST'])
def app_home(request,*args, **kwargs):
    # model_data=Products.objects.all().order_by('?').first()
    instance=Products.objects.all().order_by('?').first()
   
    data={}
    if instance:
        # data['model_id']=model_data.id
        # data['title']=model_data.title
        # data['content']=model_data.content
        # data['price']=model_data.price
        # data=model_to_dict(instance,fields=['id','title','price','sale_price'])
        data=ProductSerializer(instance).data
     
    return Response(data)
        # data={}
    # data['params']=dict(request.GET)
    # data['content_type']=request.content_type
    # return JsonResponse(data)
'''

@api_view(['POST'])
def app_home(request,*args, **kwargs):
    # model_data=Products.objects.all().order_by('?').first()
    serializer=ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance=serializer.save()
        print(instance)
        return Response(serializer.data)
    return Response({'message':'invalid data-type'},status=400)

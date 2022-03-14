from tracemalloc import get_object_traceback
from rest_framework import generics
from .models import Products
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
 
 
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset=Products.objects.all()
    serializer_class=ProductSerializer

    def perform_create(self, serializer):
        a=serializer.validated_data
        print(a)
        title=a.get('title')
        price=a.get('price')
        content=a.get('content')
        if content is None:
            content=title
        serializer.save(content=content)
        
        
    
productlistcreateview=ProductListCreateAPIView.as_view()
    
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset=Products.objects.all()
    serializer_class=ProductSerializer
    #look_up field='pk'
    

@api_view(['GET','POST'])
def product_alt_view(request,pk=None,*args, **kwargs):
    method=request.method 
    if method=='GET':
        #listview
        #get_request -> details view
        if 'pk' is not None:
            obj=get_object_or_404(Products,pk=pk)
            data=ProductSerializer(obj,many=False).data
            return Response(data)
        
        queryset=Products.objects.all()
        data=ProductSerializer(queryset,many=True).data
        return Response(data)
    
    if method=='POST':
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title=serializer.validated_data.get('title')
            content=serializer.validated_data.get('content') or None
            if content is None:
                content=title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"message":'invalid'},status=400)
                
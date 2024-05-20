from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import response
from products.models import Product, User
from products.serializers import ProductSerializer
import random
# Create your views here.

class ProductViewSet(viewsets.ViewSet):
    def list(self, request): #/api/products
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return response.Response(serializer.data)
    
    def create (self, request): #/api/products
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        else:
            return response.Response(serializer.errors)
    
    def retrieve(self, request, pk=None): #/api/products/<str:id>
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product, many=False)
        return response.Response(serializer.data)
    
    def update(self, request, pk=None): #/api/products/<str:id>
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        else:
            return response.Response(serializer.errors)
    
    def destroy(self, request, pk=None): #/api/products/<str:id>
        product = Product.objects.get(id=pk)
        product.delete()
        return response.Response('Product Deleted')


class UserApiViewSet(viewsets.ViewSet):
    def get(self, request):
        users = User.objects.all()
        user = random.choice(users)
        return response.Response({'id': user.id})
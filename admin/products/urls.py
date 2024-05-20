from django.contrib import admin
from django.urls import path
from products.views import ProductViewSet
from products.views import UserApiViewSet

urlpatterns = [
    path('products', ProductViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('products/<str:pk>', ProductViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('user', UserApiViewSet.as_view({ 'get': 'get' }))
]

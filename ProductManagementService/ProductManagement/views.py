from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *
# from ...UserAuthenticationService.users.producer import publish

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = [ 'productCategory']

    # def create(self, request, *args, **kwargs):
    #     response = super().create(request, *args, **kwargs)

    #     user_id = '1'  #PAXI JWT DECODE GARERA YESMA ID HALNI
    #     product_id = response.data.get('id')  

    #     # Publish the message to RabbitMQ
    #     publish(user_id, product_id)

    #     return response

class FavProdViewSet(ModelViewSet):
    queryset = FavProducts.objects.all()
    serializer_class = FavProductsSerializer

    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = [ 'user_id', 'product_id']

   


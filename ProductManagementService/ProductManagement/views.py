from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = [ 'productCategory']
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Product
from .permissions import GetOrIsStaff
from .serializers import ProductSerializer
from rest_framework.authentication import TokenAuthentication

class ProductView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [GetOrIsStaff]

    def perform_create(self, serializer):
        #serializer.save()
        ...

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [GetOrIsStaff]
    serializer_class = ProductSerializer
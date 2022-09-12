from unicodedata import category
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Product
from .permissions import GetOrIsStaff
from .serializers import ProductSerializer
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import get_object_or_404
from discounts.models import Discount
from categories.models import Category

class ProductView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [GetOrIsStaff]
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        try:
            category_obj = get_object_or_404(Category, pk=self.request.data["category_id"])
        except:
            category_obj = get_object_or_404(Category, pk=1)
        try:
            self.request.data["discount_id"]
            discount_obj = get_object_or_404(Discount, pk=self.request.data["discount_id"])
        except:
            discount_obj = get_object_or_404(Discount, pk=1)

        serializer.save(product_category=category_obj, product_discount=discount_obj)

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [GetOrIsStaff]
    serializer_class = ProductSerializer

    def perform_update(self, serializer):

        try:
            category_obj = get_object_or_404(Category, pk=self.request.data["category_id"])
        except:
            category_obj = get_object_or_404(Category, pk=1)
        try:
            self.request.data["discount_id"]
            discount_obj = get_object_or_404(Discount, pk=self.request.data["discount_id"])
        except:
            discount_obj = get_object_or_404(Discount, pk=1)

        serializer.save(product_category=category_obj, product_discount=discount_obj)
from unicodedata import category
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Product
from .permissions import GetOrIsStaff
from .serializers import ProductSerializer, ProductDetailSerializer
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
        get_category = self.request.data.get("category_id", None)

        get_discount = self.request.data.get("discount_id", None)

        discount_obj = get_object_or_404(Discount, pk=1)

        category_obj = Category.objects.filter(pk=1)
        
        if get_category:
            category_obj = Category.objects.filter(pk__in=self.request.data["category_id"])
        if get_discount:
            discount_obj = get_object_or_404(Discount, pk=self.request.data["discount_id"])

        serializer.save(product_category=category_obj, product_discount=discount_obj)

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [GetOrIsStaff]
    serializer_class = ProductDetailSerializer

    def perform_update(self, serializer):
        get_category = self.request.data.get("category_id", None)
        if get_category:
            category_obj = Category.objects.filter(pk__in=self.request.data["category_id"])
            serializer.save(product_category=category_obj)
                
        get_discount = self.request.data.get("discount_id", None)

        if get_discount:
            discount_obj = get_object_or_404(Discount, pk=self.request.data["discount_id"])
            serializer.save(product_discount=discount_obj)

        serializer.save()
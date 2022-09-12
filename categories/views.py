from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Category
from .permissions import GetOrIsStaff
from rest_framework.authentication import TokenAuthentication
from .serializers import CategorySerializer

class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [GetOrIsStaff]
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [GetOrIsStaff]
    serializer_class = CategorySerializer
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Discount
from .permissions import GetOrIsStaff
from rest_framework.authentication import TokenAuthentication
from .serializers import DiscountSerializer

class DiscountView(generics.ListCreateAPIView):
    queryset = Discount.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [GetOrIsStaff]
    serializer_class = DiscountSerializer

class DiscountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discount.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [GetOrIsStaff]
    serializer_class = DiscountSerializer
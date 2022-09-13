from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView, Request, Response, status
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication



# from .mixins import SerializerByMethodMixin
from .models import Cart
from .permissions import IsUserOwnerOrAdminOrStaff

from .serializers import CartSerializer

class CartView(generics.RetrieveAPIView):
    queryset = Cart.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsUserOwnerOrAdminOrStaff]
    serializer_class = CartSerializer
    lookup_url_kwarg = 'cart_id'


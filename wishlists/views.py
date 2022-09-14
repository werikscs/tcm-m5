from unittest import expectedFailure
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView, Request, Response, status
from rest_framework import generics
from django.core.exceptions import ValidationError


from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.pagination import PageNumberPagination

import ipdb

from .mixins import SerializerByMethodMixin
from .models import Wishlist
from users.models import User
from products.models import Product
from .permissions import IsOwnerOrAdminOrStaff

from .serializers import WishlistSerializer, WishlistGetSerializer


# Create your views here.




class UserWishlistView(SerializerByMethodMixin , generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrAdminOrStaff]
    serializer_map = {
        "GET": WishlistGetSerializer,
        "POST": WishlistSerializer,
    }
    

    def perform_create(self, serializer):
        user = get_object_or_404(User, pk=self.kwargs["user_id"])
        product = get_object_or_404(Product, id=self.request.data["product"])
        
        
        serializer.save(user_id=user.id)
    
    def get_queryset(self):
        user = get_object_or_404(User, pk=self.kwargs["user_id"])

        return Wishlist.objects.filter(user_id=user)


class UserWishlistDetailView(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrAdminOrStaff]
    serializer_class = WishlistSerializer
    lookup_url_kwarg = 'wishlist_id'

    def get_queryset(self):
        user = get_object_or_404(User, pk=self.kwargs["user_id"])

        return Wishlist.objects.filter(user_id=user)
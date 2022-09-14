from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from users.models import User

from orders.models import Order
from orders.permissions import IsOwnerOrAdminOrStaff

from .serializers import OrderSerializer


# Create your views here.
class OrderView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrAdminOrStaff]
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = get_object_or_404(User, pk=self.kwargs["user_id"])

        return Order.objects.filter(user_id=user)


class OrderDetailView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrAdminOrStaff]
    serializer_class = OrderSerializer
    lookup_url_kwarg = "order_id"

    def get_queryset(self):
        user = get_object_or_404(User, pk=self.kwargs["user_id"])

        return Order.objects.filter(user_id=user)

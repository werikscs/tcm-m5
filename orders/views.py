from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from orders.models import Order

from .serializers import OrderSerializer


# Create your views here.
class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    authentication_classes = [TokenAuthentication]
    serializer_class = OrderSerializer

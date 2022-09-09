from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView, Request, Response, status
from rest_framework import generics



from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.pagination import PageNumberPagination



from .mixins import SerializerByMethodMixin
from .models import User
from .permissions import IsAdminOrOwner, IsAdminToGet

from .serializers import UserSerializer, StaffUserSerializer, PatchUserSerializer, DeleteOrChangeUserSerializer


class UserRegisterView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminToGet]
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserRegisterStaff(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = StaffUserSerializer
    queryset = User.objects.all()


class UserDetailView(SerializerByMethodMixin ,generics.RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrOwner]

    serializer_map = {
        "GET": UserSerializer,
        "PATCH": PatchUserSerializer,
    }
    # serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_url_kwarg = 'user_id'

class UserDeleteOrChangeView(generics.RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = DeleteOrChangeUserSerializer
    queryset = User.objects.all()
    lookup_url_kwarg = 'user_id'
   


class LoginView(ObtainAuthToken):
    
    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )

        serializer.is_valid(raise_exception=True)
        
        user = serializer.validated_data["user"]
        token, _ = Token.objects.get_or_create(user=user)

        return Response({"token": token.key})

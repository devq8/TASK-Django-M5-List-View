from rest_framework.generics import CreateAPIView
from .serializer import UserCreateSerializer

class UserCreateAPIView(CreateAPIView):
    serializer_class= UserCreateSerializer
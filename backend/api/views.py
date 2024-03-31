from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from res_framework.permissions import IsAuthenticated, AllowAny


class CreateUserView(generics.CreateAPIView):
    """
    Create a new user in the system
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
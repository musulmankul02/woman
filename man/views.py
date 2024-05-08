from django.shortcuts import render
from rest_framework import generics
from .serializer import ManSerializer

from .models import Man
# Create your views here.

class ManAPIViews(generics.ListAPIView):
    queryset = Man.objects.all()
    serializer_class = ManSerializer
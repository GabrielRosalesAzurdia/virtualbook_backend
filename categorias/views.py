from django.shortcuts import render
from rest_framework import viewsets
from .models import Categories
from .serializers import CategorySerializer
# Create your views here.

class CategoryView(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
from django.shortcuts import render
from .serializers import AutoresSerializar
from .models import Autors
from rest_framework import viewsets
from .paginator import MyOffsetPagination
from .serializers import AutoresSerializar
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
# Create your views here.

class AutoresView(viewsets.ModelViewSet):
    queryset = Autors.objects.all()
    serializer_class = AutoresSerializar
    pagination_class = MyOffsetPagination

# @api_view(['GET'])
# def AutorPorId(request, autor_id):
#     queryset = Autors.objects.filter(autor_id = autor_id)
#     serializer = AutoresSerializar(queryset, many=False,context={"request": request})
#     Rensponse(serializer.data)
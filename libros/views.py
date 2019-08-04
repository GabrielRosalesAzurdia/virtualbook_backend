from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import LibrosSerializar
from .paginator import MyOffsetPagination
from django.shortcuts import render
from rest_framework import viewsets
from autores.models import Autors
from .models import Libros
# Create your views here.

# Clase que envia todos los libros y tambien envia el que se le envie la id
class LibrosView(viewsets.ModelViewSet):
    queryset = Libros.objects.all()
    serializer_class = LibrosSerializar
    pagination_class = MyOffsetPagination

# Busca los libros que se le indiquen y los pagina
@api_view(['GET'])
@permission_classes((AllowAny, ))  
def BookssSearchView(request,palabra_clave):
    list_found = []
    key1 = Libros.objects.filter(name__contains = palabra_clave)
    key2 = Libros.objects.filter(description__contains = palabra_clave)
    queryset = key1 | key2

    paginator = PageNumberPagination()
    paginator.page_size = 10
    person_objects = queryset
    result_page = paginator.paginate_queryset(person_objects, request)
    serializer = LibrosSerializar(result_page, many=True,context={"request": request})
    return paginator.get_paginated_response(serializer.data)


# @api_view(['GET'])
# @permission_classes((AllowAny, ))  
# def Books(request,id_libro):

#     queryset1 = libros.objects.filter(id_libro = book_id)
#     queryset2 = Autors.objects.all()
#     queryset = []

#     for i in range(len(queryset1)):
#         queryset2 = queryset2.filter(product_id = queryset1[i].product_id.product_id)
#         if queryset == []:
#             queryset = queryset2
#         else: 
#             queryset = queryset | queryset2
#         queryset2 = Product.objects.all()

    # paginator = PageNumberPagination()
    # paginator.page_size = 10
    # person_objects = queryset
    # result_page = paginator.paginate_queryset(person_objects, request)
    # serializer = productoSerialiser(result_page, many=True,context={"request": request})
    # return paginator.get_paginated_response(serializer.data)
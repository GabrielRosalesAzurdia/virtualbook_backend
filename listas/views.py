from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import viewsets
from libros.models import Libros 
from .models import ListaDeseos, ListaRenta
from .serializers import ListaDeseosSerializer, ListaRentaSerializer, BookinList
from .forms import ListaDeseosFormCreate, ListaRentaFormCreate
from datetime import datetime, date, time, timedelta
import calendar
import uuid
# Create your views here.

#Genera una id unica para el carrito de compras de cada usuario
@api_view(['GET'])
def GenerateShippingCart(request):
    genereted_id = str(uuid.uuid4())
    genereted_id = genereted_id.replace("-","")
    union_ids = str(genereted_id) 
    return Response({ "cart_id" : union_ids })

#Crea una lista de deseos con los datos requeridos en el modelo y formulario
@api_view(['POST'])
def ListaDeseosCreateview(request):
    form = ListaDeseosFormCreate(request.data)
    if form.is_valid():
        maybe = True
        post = form.save(commit=False)
        queryset = ListaDeseos.objects.all().filter(cart_id = post.cart_id)
        for i in range(len(queryset)):
            if post.book_id == queryset[i].book_id:
                maybe = False
        if maybe == True:
            post.save()
            return Response("Funciono")
        elif maybe == False:
            return Response("Fallo")   
    else:
        return Response("Fallo")   

#Crea una lista de rentados con los datos requeridos en el modelo y formulario
@api_view(['POST'])
def ListaRentaCreateview(request):
    form = ListaRentaFormCreate(request.data)
    if form.is_valid():
        maybe = True
        post = form.save(commit=False)
        queryset = ListaRenta.objects.all().filter(cart_id = post.cart_id)
        queryset_2 = ListaDeseos.objects.all().filter(cart_id = post.cart_id)
        queryset_2 = queryset_2.filter(book_id = post.book_id)
        for i in range(len(queryset)):
            if post.book_id == queryset[i].book_id:
                maybe = False

        if len(queryset) > 4:
            print(len(queryset))
            maybe = False

        if maybe == True:
            if len(queryset_2) != 0:
                queryset_2.delete()
            post.save()
            return Response("Funciono")
        elif maybe == False:
            return Response("Fallo en otra cosa")   
    else:
        return Response("Fallo formulario")   

#Encuentra y envia una lista de deseos enlazados con la misma cart_id
@api_view(['GET'])
def ListaDeseosView(request,id_cart):
    cart_id = ListaDeseos.objects.filter(cart_id=id_cart)
    resultados = []
    prueba = {}
    for i in range(len(cart_id)):
        product_found = Libros.objects.filter(book_id = cart_id[i].book_id)
        product_serializer = BookinList(product_found[0], context={"request": request})
        serializer = ListaDeseosSerializer(cart_id[i] ,context={"request": request})
        prueba.update(serializer.data)
        prueba.update(product_serializer.data)
        resultados.append(prueba)
        prueba = {}
    return Response( resultados )

#Encuentra y envia una lista de rentados enlazados con la misma cart_id
@api_view(['GET'])
def ListaRentaView(request,id_cart):
    cart_id = ListaRenta.objects.filter(cart_id=id_cart)
    resultados = []
    prueba = {}
    for i in range(len(cart_id)):
        product_found = Libros.objects.filter(book_id = cart_id[i].book_id)
        product_serializer = BookinList(product_found[0], context={"request": request})
        serializer = ListaRentaSerializer(cart_id[i] ,context={"request": request})
        prueba.update(serializer.data)
        prueba.update(product_serializer.data)
        resultados.append(prueba)
        prueba = {}
    return Response( resultados )

#Elimina todos los elementos en la misma lista de deseos
@api_view(['DELETE'])
def ListaDeseosDeleteView(request,id_cart):
    ListaDeseos.objects.filter(cart_id = id_cart).delete()
    return Response( [] )

#Elimina todos los elementos en la misma lista de rendatos
@api_view(['DELETE'])
def ListaRentaDeleteView(request,id_cart):
    ListaRenta.objects.filter(cart_id = id_cart).delete()
    return Response( [] )

# encuentra y elimina un elemnto de la lista de deseos
@api_view(['DELETE'])
def deseos_delete_item(request,id_item):
    ListaDeseos.objects.filter(lista_deseos_id = id_item).delete()
    return Response("Se ha eliminado")

# encuentra y elimina un elemnto de la lista de rentados
@api_view(['DELETE'])
def rentados_delete_item(request,id_item):
    ListaRenta.objects.filter(lista_rentados_id = id_item).delete()
    return Response("Se ha eliminado")


@api_view(['GET'])
def revisionFechas(request,cart_id):
    print("revisando fechas")
    queryset = ListaRenta.objects.all().filter(cart_id = cart_id)
    fecha_actual = date.today()  
    maybe = False
    if len(queryset) > 0:
        for i in range(len(queryset)):
            print(queryset[i].deleted_on <= fecha_actual);
            if queryset[i].deleted_on <= fecha_actual:
                queryset[i].delete()
                maybe = True
    if maybe:
        return Response("Se ha eliminado")
    else:
        return Response("No se ha eliminado ninguno") 

#Moeve un elemento de shopping_cart haciendo que su buy_now sea verdadero
# @api_view(['GET'])
# def shopping_cart_move(request,id_item):
#     queryset = shopping_cart.objects.filter(item_id = id_item)
#     a = queryset[0]
#     a.buy_now = True
#     a.save()
#     return Response(["movido",str(a.buy_now)])
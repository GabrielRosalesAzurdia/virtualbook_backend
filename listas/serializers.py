from rest_framework import serializers
from libros.models import Libros
from .models import ListaDeseos, ListaRenta

class ListaDeseosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaDeseos
        fields = ("lista_deseos_id","cart_id","book_id","added_on")

class ListaRentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaRenta
        fields = ("lista_rentados_id","cart_id","book_id","added_on","deleted_on")

class BookinList(serializers.ModelSerializer):
    class Meta:
        model = Libros
        fields = ("book_id","name","image","description") 
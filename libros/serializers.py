from rest_framework import serializers
from .models import Libros

class LibrosSerializar(serializers.ModelSerializer):
    class Meta:
        model = Libros
        fields = ("book_id","name","description","image","autor_id","category_id")
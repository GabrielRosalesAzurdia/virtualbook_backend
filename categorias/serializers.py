from .models import Categories
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ("categorie_id", "name", "description") 
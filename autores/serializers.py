from rest_framework import serializers
from .models import Autors

class AutoresSerializar(serializers.ModelSerializer):
    class Meta:
        model = Autors
        fields = ("autor_id","name","birthday","dead_day","litle_biografy")
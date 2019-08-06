from django.contrib.auth import get_user_model

from rest_framework import serializers

#convierte el modelo usuario a objeto json
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'customer_id',
            'email',
            'first_name',
            'last_name',
            'password',
            'credit_card',
            'imagen',
            'address_1',
            'address_2',
            'city',
            'region',
            'postal_code',
            'country',
            'day_phone',
            'eve_phone',
            'mob_phone',
        ]
        write_only_fields = ['password']

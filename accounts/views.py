from .forms import UserCreationForm, UserUpdateForm,UserUpdateCreditCartForm
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from django.core.serializers import serialize
from rest_framework.response import Response
from .serializers import UserSerializer
from django.shortcuts import render
from rest_framework import viewsets
from .models import User


#manejo basico de usuario
class CustomerView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request):
        #Trae todos los usuario
        if request.method == "GET":
            queryset = User.objects.all()
            user = get_object_or_404(queryset, email=request.user.email)
            serializer = UserSerializer(user)
            return Response(serializer.data)

        #Actualiza un usuario
        if request.method == "PUT":
            queryset = User.objects.all()
            user = get_object_or_404(queryset, email=request.user.email)
            form = UserUpdateForm(request.data, instance=user)
            if form.is_valid():
                form.save()
                return Response(str("Hecho"))
            else:
                return Response(str("MAL"))

#Registra un usuario en la paguina
@api_view(['PUT'])
@permission_classes((AllowAny, ))  
def customerRegister(request):
    form = UserCreationForm(request.data)
    if form.is_valid():
        form.save()
        return Response( str(True) )
    else:
        return Response( str(False) )

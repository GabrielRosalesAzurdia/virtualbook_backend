from django import forms
from .models import ListaDeseos, ListaRenta

#formulario para añadir un producto al shipping cart
class ListaDeseosFormCreate(forms.ModelForm):
    class Meta:
        model = ListaDeseos
        fields = '__all__'

#formulario para crear una orden
class ListaRentaFormCreate(forms.ModelForm):
    class Meta:
        model = ListaRenta
        fields = '__all__'
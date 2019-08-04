from django.db import models
from datetime import datetime, date, time, timedelta
import calendar

print("Fechas:")
# Asigna fecha actual
fecha1 = date.today()   
print("\tFecha1:", fecha1)
# Suma a la fecha actual 2 días
fecha2 = date.today() + timedelta(days=10)
print("\tFecha2:", fecha2)


# Create your models here.

class ListaDeseos(models.Model):
    lista_deseos_id = models.AutoField(primary_key=True)
    cart_id = models.TextField()
    book_id = models.IntegerField()
    added_on = models.DateField(auto_now_add=True, blank=True)

class ListaRenta(models.Model):
    lista_rentados_id = models.AutoField(primary_key=True)
    cart_id = models.TextField()
    book_id = models.IntegerField()
    added_on = models.DateField(default=fecha1, blank=True)
    deleted_on = models.DateField(default=fecha2, blank=True)
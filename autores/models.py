from django.db import models

# Create your models here.

class Autors(models.Model):
    autor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    birthday = models.DateField()
    dead_day = models.DateField(blank = True,null=True)
    litle_biografy = models.CharField(max_length=250)

    def __str__(self):
        return self.name
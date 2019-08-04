from django.db import models

# Create your models here.

class Libros(models.Model):
    book_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)    
    description = models.TextField()
    published_date = models.DateField()
    image =  models.ImageField(upload_to="images")
    autor_id = models.ForeignKey("autores.Autors", on_delete=models.CASCADE)
    category_id = models.ForeignKey("categorias.Categories", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
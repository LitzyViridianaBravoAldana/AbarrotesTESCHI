from django.db import models

# Create your models here.

class Categoria(models.Model):
    id_Categoria = models.AutoField(primary_key=True,db_column='Id_Categoria')
    Descripcion = models.TextField(db_column='Descripcion')
    class Meta:
        db_table='Categorias'
class Pais(models.Model):
    Id_Pais = models.AutoField(primary_key=True,db_column='Id_Pais')
    Descripcion = models.TextField(db_column='Descripcion')
    Codigo_Idioma = models.TextField(db_column='Codigo_Idioma')
    class Meta:
        db_table='Paises'

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
    Codigo_Pais = models.TextField(db_column='Codigo_Pais')
    class Meta:
        db_table='Paises'
class Idioma(models.Model):
    Id_Idioma = models.AutoField(primary_key=True,db_column='Id_Idioma')
    Descripcion = models.TextField(db_column='Descripcion')
    Codigo_Idioma = models.TextField(db_column='Codigo_Idioma')
    class Meta:
        db_table='Idiomas'
class Editorial(models.Model):
    Id_Editorial = models.AutoField(primary_key=True,db_column='Id_Editorial')
    fk_pais = models.ForeignKey(Pais,on_delete=models.CASCADE,default=1,db_column='fk_pais')
    Nombre_Editorial = models.TextField(db_column='Nombre_Editorial')
    Sitio_Web = models.URLField(db_column='Sitio_Web')
    class Meta:
        db_table='Editoriales'
class Autor(models.Model):
    Id_Autor = models.AutoField(primary_key=True,db_column='Id_Autor')
    Fk_pais = models.ForeignKey(Pais,on_delete=models.CASCADE,default=1,db_column='fk_pais')
    Nombre = models.CharField(max_length=25,db_column='Nombre')
    Apellido_P = models.CharField(max_length=20,db_column='Apellido_P')
    Apellido_M = models.CharField(max_length=20,db_column='Apellido_M')
    Biografia = models.CharField(max_length=200,db_column='Biografia')
    class Meta:
        db_table='Autores'
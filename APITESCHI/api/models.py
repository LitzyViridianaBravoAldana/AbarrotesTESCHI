from django.db import models

# Create your models here.
class Usuario(models.Model):
    id_Usuarios = models.AutoField(primary_key=True,db_column='Id_Usuario')
    Nombre_Usuario = models.TextField(db_column='Nombre_Usuario')
    Contrasena = models.TextField(db_column='Contrasena')
    Nombre = models.TextField(db_column='Nombre')
    Correo = models.EmailField(db_column='Correo')
    class Meta:
        db_table='Usuarios'
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

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


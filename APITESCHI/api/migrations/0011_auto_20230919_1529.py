# Generated by Django 3.2.4 on 2023-09-19 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_libro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='editorial',
            name='fk_pais',
        ),
        migrations.RemoveField(
            model_name='libro',
            name='Fk_Id_Autor',
        ),
        migrations.RemoveField(
            model_name='libro',
            name='Fk_Id_Editorial',
        ),
        migrations.RemoveField(
            model_name='libro',
            name='Fk_Id_Genero',
        ),
        migrations.RemoveField(
            model_name='libro',
            name='Fk_Id_Idioma',
        ),
        migrations.DeleteModel(
            name='Autor',
        ),
        migrations.DeleteModel(
            name='Editorial',
        ),
        migrations.DeleteModel(
            name='Libro',
        ),
    ]
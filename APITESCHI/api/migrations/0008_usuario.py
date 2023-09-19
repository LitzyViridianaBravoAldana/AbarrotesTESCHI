# Generated by Django 3.2.4 on 2023-09-19 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20230919_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_Usuarios', models.AutoField(db_column='Id_Usuario', primary_key=True, serialize=False)),
                ('Nombre_Usuario', models.TextField(db_column='Nombre_Usuario')),
                ('Contrasena', models.TextField(db_column='Contrasena')),
                ('Nombre', models.TextField(db_column='Nombre')),
                ('Apellido_Pa', models.CharField(db_column='Apellido_P', max_length=20)),
                ('Apellido_Ma', models.CharField(db_column='Apellido_M', max_length=20)),
                ('Telefono', models.IntegerField(db_column='Telefono', max_length=10)),
                ('Correo', models.EmailField(db_column='Correo', max_length=254)),
            ],
            options={
                'db_table': 'Usuarios',
            },
        ),
    ]
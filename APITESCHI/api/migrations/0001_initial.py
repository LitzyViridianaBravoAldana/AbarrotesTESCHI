# Generated by Django 3.2.4 on 2023-09-19 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_Usuarios', models.AutoField(db_column='Id_Usuario', primary_key=True, serialize=False)),
                ('Nombre_Usuario', models.TextField(db_column='Nombre_Usuario')),
            ],
            options={
                'db_table': 'Usuarios',
            },
        ),
    ]
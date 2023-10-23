# Generated by Django 3.2.4 on 2023-10-11 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_auto_20231010_1840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='password',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='Contrasena',
            field=models.TextField(db_column='Contrasena'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='Nombre_Usuario',
            field=models.TextField(db_column='Nombre_Usuario', default='manuel', unique=True),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='usuario',
            table='Usuarios',
        ),
    ]
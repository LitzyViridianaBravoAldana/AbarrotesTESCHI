# Generated by Django 3.2.4 on 2023-10-11 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_auto_20231010_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='Contrasena',
            field=models.TextField(db_column='Contrasena'),
        ),
    ]

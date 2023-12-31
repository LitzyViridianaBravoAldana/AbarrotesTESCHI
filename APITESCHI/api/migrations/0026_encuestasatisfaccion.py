# Generated by Django 3.2.4 on 2023-10-19 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_auto_20231010_1903'),
    ]

    operations = [
        migrations.CreateModel(
            name='encuestaSatisfaccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_encuesta', models.TextField(db_column='id_encuesta')),
                ('correo', models.TextField(db_column='Dirección de correo electrónico')),
                ('pregunta1', models.TextField(db_column='¿Qué tipo de paleta de colores prefieres para el diseño del sistema web de la biblioteca?')),
                ('pregunta2', models.TextField(db_column='¿Qué opinas sobre la personalización de tu perfil en el sistema web de la biblioteca?')),
                ('pregunta3', models.TextField(db_column='¿Cómo te gustaría que se presenten los resultados de búsqueda en el sistema web de la biblioteca?')),
                ('pregunta4', models.TextField(db_column='¿Cuál de las siguientes opciones de búsqueda preferirías en el sistema web de la biblioteca?')),
                ('pregunta5', models.TextField(db_column='¿Qué función consideras más importante para un acceso rápido en la página principal del sistema web de la biblioteca?')),
                ('pregunta6', models.TextField(db_column='¿Dónde preferirías ver las notificaciones en el sistema web de la biblioteca?')),
                ('pregunta7', models.TextField(db_column='¿Te gustaría poder personalizar las notificaciones que recibes en el sistema web de la biblioteca?')),
            ],
            options={
                'db_table': 'encuestaSatisfaccion',
            },
        ),
    ]

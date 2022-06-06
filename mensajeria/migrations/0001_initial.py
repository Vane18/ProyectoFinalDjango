# Generated by Django 4.0.4 on 2022-06-06 15:33

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creador_id', models.IntegerField()),
                ('creador_usuario', models.TextField(max_length=50)),
                ('mensaje', tinymce.models.HTMLField()),
                ('fecha', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remitente_id', models.IntegerField()),
                ('remitente_usuario', models.TextField(max_length=50)),
                ('destinatario_id', models.IntegerField()),
                ('destinatario_usuario', models.TextField(max_length=50)),
                ('mensaje', models.TextField(max_length=500)),
                ('fecha', models.DateTimeField()),
                ('visto', models.CharField(max_length=2)),
            ],
        ),
    ]

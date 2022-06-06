# Generated by Django 4.0.4 on 2022-06-05 17:54

import AplicacionPrincipal.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AplicacionPrincipal', '0005_remove_avatar_imagen_avatar_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posteo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.TextField(max_length=50)),
                ('fecha', models.DateField()),
                ('titulo', models.TextField(max_length=50)),
                ('descripcion', models.TextField(max_length=500)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to=AplicacionPrincipal.models.filepath)),
            ],
        ),
    ]

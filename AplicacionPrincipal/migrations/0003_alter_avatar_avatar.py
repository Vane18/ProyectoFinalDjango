# Generated by Django 4.0.4 on 2022-06-05 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AplicacionPrincipal', '0002_remove_avatar_imagen_avatar_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
    ]

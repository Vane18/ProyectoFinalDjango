# Generated by Django 4.0.4 on 2022-06-05 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AplicacionPrincipal', '0004_rename_avatar_avatar_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avatar',
            name='imagen',
        ),
        migrations.AddField(
            model_name='avatar',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatar'),
        ),
    ]

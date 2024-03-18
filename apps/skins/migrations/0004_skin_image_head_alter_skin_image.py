# Generated by Django 5.0.1 on 2024-03-18 14:58

import apps.skins.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skins', '0003_skin_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='skin',
            name='image_head',
            field=models.ImageField(blank=True, null=True, upload_to='skins/images/head/'),
        ),
        migrations.AlterField(
            model_name='skin',
            name='image',
            field=models.ImageField(upload_to=apps.skins.models.skin_image_filename),
        ),
    ]

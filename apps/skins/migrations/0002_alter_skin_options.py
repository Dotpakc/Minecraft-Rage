# Generated by Django 5.0.1 on 2024-03-01 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skins', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skin',
            options={'ordering': ['-created_at'], 'verbose_name': 'Skin', 'verbose_name_plural': 'Skins'},
        ),
    ]

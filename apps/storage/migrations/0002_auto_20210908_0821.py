# Generated by Django 2.0.6 on 2021-09-08 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image1',
            field=models.URLField(default='https://i.postimg.cc/NMdGGd18/imagen-lista-producto-sin-foto-2-25fa77.png', max_length=1000),
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.URLField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]

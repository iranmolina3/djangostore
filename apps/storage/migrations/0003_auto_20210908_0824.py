# Generated by Django 2.0.6 on 2021-09-08 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0002_auto_20210908_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.URLField(default='https://i.postimg.cc/NMdGGd18/imagen-lista-producto-sin-foto-2-25fa77.png', max_length=1000),
        ),
    ]
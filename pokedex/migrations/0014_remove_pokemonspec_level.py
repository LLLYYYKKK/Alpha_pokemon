# Generated by Django 2.0.6 on 2018-07-01 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0013_auto_20180702_0003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemonspec',
            name='level',
        ),
    ]

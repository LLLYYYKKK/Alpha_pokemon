# Generated by Django 2.0.6 on 2018-06-30 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0006_pokemonability_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonability',
            name='description',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='pokedex.Description'),
        ),
    ]

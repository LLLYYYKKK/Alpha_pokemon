# Generated by Django 2.0.6 on 2018-07-14 10:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import pokedex.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pokedex', '0016_auto_20180706_2219'),
    ]

    operations = [
        migrations.CreateModel(
            name='SamplePokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(default=50, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('hp_EV', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(252)])),
                ('attack_EV', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(252)])),
                ('defense_EV', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(252)])),
                ('sp_attack_EV', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(252)])),
                ('sp_defense_EV', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(252)])),
                ('speed_EV', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(252)])),
                ('hp_IV', models.IntegerField(default=31, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(31)])),
                ('attack_IV', models.IntegerField(default=31, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(31)])),
                ('defense_IV', models.IntegerField(default=31, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(31)])),
                ('sp_attack_IV', models.IntegerField(default=31, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(31)])),
                ('sp_defense_IV', models.IntegerField(default=31, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(31)])),
                ('speed_IV', models.IntegerField(default=31, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(31)])),
                ('nature', models.ForeignKey(default=pokedex.models.PokemonNature(1, 44, 45, 46), on_delete=django.db.models.deletion.CASCADE, to='pokedex.PokemonNature')),
                ('spec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokedex.PokemonSpec')),
            ],
        ),
    ]
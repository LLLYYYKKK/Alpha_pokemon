# Generated by Django 2.0.6 on 2018-07-06 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0015_auto_20180702_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='name',
            name='english',
            field=models.CharField(default='No name', max_length=20),
        ),
        migrations.AlterField(
            model_name='name',
            name='korean',
            field=models.CharField(default='이름 없음', max_length=20),
        ),
    ]

# Generated by Django 2.0 on 2020-02-29 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='imdb_score',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='popularity_99',
            field=models.FloatField(),
        ),
    ]
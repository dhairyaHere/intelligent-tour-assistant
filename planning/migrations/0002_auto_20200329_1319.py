# Generated by Django 2.2.11 on 2020-03-29 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='place_distance',
            field=models.CharField(max_length=10),
        ),
    ]

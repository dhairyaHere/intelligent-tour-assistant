# Generated by Django 2.2.11 on 2020-04-23 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0002_auto_20200329_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip_details',
            name='category',
            field=models.CharField(default=1234, max_length=20),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.1.3 on 2020-11-19 22:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0002_auto_20201119_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 11, 19, 22, 47, 44, 41912)),
        ),
    ]

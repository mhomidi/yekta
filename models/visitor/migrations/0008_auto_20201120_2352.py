# Generated by Django 3.1.3 on 2020-11-20 20:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0007_auto_20201120_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 20, 23, 52, 44, 957207)),
        ),
    ]

# Generated by Django 3.1.3 on 2020-11-20 14:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0005_auto_20201120_0222'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='ip',
            field=models.CharField(default='0.0.0.0', max_length=17),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 20, 18, 12, 20, 946521)),
        ),
    ]

# Generated by Django 3.1.1 on 2021-01-06 12:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 6, 12, 4, 5, 260745, tzinfo=utc)),
        ),
    ]

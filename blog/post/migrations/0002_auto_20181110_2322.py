# Generated by Django 2.0.9 on 2018-11-10 21:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 10, 21, 22, 13, 358944, tzinfo=utc)),
        ),
    ]

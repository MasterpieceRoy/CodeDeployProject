# Generated by Django 2.1.3 on 2018-11-06 12:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20181106_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='date_updated',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 6, 12, 16, 40, 1825, tzinfo=utc)),
        ),
    ]

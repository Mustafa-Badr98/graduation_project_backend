# Generated by Django 4.2.6 on 2023-10-15 18:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_newuser_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 15, 18, 54, 13, 360877, tzinfo=datetime.timezone.utc)),
        ),
    ]

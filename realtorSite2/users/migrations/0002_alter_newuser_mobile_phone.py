# Generated by Django 4.2.6 on 2023-11-06 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='mobile_phone',
            field=models.IntegerField(),
        ),
    ]

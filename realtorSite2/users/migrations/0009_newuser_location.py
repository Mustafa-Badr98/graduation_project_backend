# Generated by Django 4.2.6 on 2023-11-08 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_newuser_mobile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='location',
            field=models.CharField(null=True),
        ),
    ]

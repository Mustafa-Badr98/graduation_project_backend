# Generated by Django 4.2.6 on 2023-10-15 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0003_rename_sell_properties_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='properties',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='properties',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-15 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_properties_created_at_properties_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='properties',
            name='area_size',
            field=models.IntegerField(null=True),
        ),
    ]
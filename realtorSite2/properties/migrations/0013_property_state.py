# Generated by Django 4.2.6 on 2023-11-13 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0012_property_offers'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='state',
            field=models.CharField(choices=[('live', 'Live'), ('sold', 'Sold')], default='live', max_length=4),
        ),
    ]
# Generated by Django 4.2.6 on 2023-11-10 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0001_initial'),
        ('properties', '0011_alter_property_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='offers',
            field=models.ManyToManyField(blank=True, null=True, related_name='property_offers', to='offers.offer'),
        ),
    ]
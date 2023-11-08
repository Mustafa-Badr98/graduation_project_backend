# Generated by Django 4.2.6 on 2023-11-07 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('properties', '0008_rename_properties_property'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='type',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='seller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='propertySeller', to=settings.AUTH_USER_MODEL, verbose_name='Seller User'),
        ),
    ]

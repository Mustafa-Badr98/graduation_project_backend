# Generated by Django 4.2.6 on 2023-10-15 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Properties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.FloatField(max_length=100)),
                ('location', models.CharField(max_length=50, null=True)),
                ('number_of_bedrooms', models.IntegerField()),
                ('number_of_bathrooms', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='accounts/properties/images/')),
            ],
        ),
    ]

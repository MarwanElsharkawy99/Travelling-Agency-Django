# Generated by Django 5.0.6 on 2024-07-01 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_package_excluded_package_included_hotel'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='img',
            field=models.ImageField(default='null', upload_to='media'),
        ),
    ]

# Generated by Django 4.2.9 on 2024-01-31 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='img',
            field=models.ImageField(default=None, upload_to='media'),
            preserve_default=False,
        ),
    ]
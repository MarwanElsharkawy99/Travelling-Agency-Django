# Generated by Django 5.0.6 on 2024-07-01 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_birth',
            field=models.DateTimeField(null=True),
        ),
    ]
# Generated by Django 5.0.6 on 2024-07-01 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0003_alter_customuser_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_birth',
            field=models.DateField(null=True),
        ),
    ]

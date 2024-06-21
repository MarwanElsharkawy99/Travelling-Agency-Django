# Generated by Django 5.0.6 on 2024-06-05 11:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_blog_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_number', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='days', to='core.package')),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_of_day', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField()),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='core.day')),
            ],
        ),
    ]

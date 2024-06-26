# Generated by Django 4.2.9 on 2024-01-29 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=250)),
                ('blog_writer', models.CharField(max_length=250)),
                ('blog_content', models.TextField()),
                ('time', models.TimeField(auto_now=True)),
            ],
        ),
    ]

# Generated by Django 2.2.28 on 2024-03-28 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendly', '0002_auto_20240328_0758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendlytoken',
            name='access_token',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='calendlytoken',
            name='refresh_token',
            field=models.CharField(max_length=1000),
        ),
    ]
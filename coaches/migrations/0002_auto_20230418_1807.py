# Generated by Django 2.2.28 on 2023-04-18 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coach',
            name='years_of_experience',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

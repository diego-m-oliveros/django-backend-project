# Generated by Django 2.2.28 on 2023-06-14 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0004_coachavailability'),
    ]

    operations = [
        migrations.AddField(
            model_name='coachavailability',
            name='is_reserved',
            field=models.BooleanField(default=False),
        ),
    ]

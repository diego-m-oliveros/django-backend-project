# Generated by Django 2.2.28 on 2023-04-30 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_emailotp'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailotp',
            name='used_for_password_reset',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 2.2.28 on 2023-04-30 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_emailotp_used_for_password_reset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailotp',
            name='otp_secret',
            field=models.CharField(max_length=32),
        ),
    ]

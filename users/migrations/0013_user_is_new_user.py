# Generated by Django 2.2.28 on 2023-04-18 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20230414_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_new_user',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 2.2.28 on 2023-10-06 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coachees', '0011_auto_20230915_1125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coacheesreviews',
            name='rate_2',
        ),
        migrations.RemoveField(
            model_name='coacheesreviews',
            name='rate_3',
        ),
        migrations.RemoveField(
            model_name='coacheesreviews',
            name='rate_4',
        ),
    ]

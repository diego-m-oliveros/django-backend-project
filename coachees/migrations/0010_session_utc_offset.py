# Generated by Django 2.2.28 on 2023-09-13 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coachees', '0009_coacheesfinalreportreview_coachfinalreportreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='utc_offset',
            field=models.DurationField(blank=True, null=True),
        ),
    ]

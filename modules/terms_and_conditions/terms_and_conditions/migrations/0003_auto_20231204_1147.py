# Generated by Django 2.2.28 on 2023-12-04 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terms_and_conditions', '0002_auto_20230424_2029'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='termandcondition',
            options={},
        ),
        migrations.AlterField(
            model_name='termandcondition',
            name='body',
            field=models.TextField(),
        ),
    ]

# Generated by Django 2.2.28 on 2023-04-24 20:29

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terms_and_conditions', '0001_terms_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='termandcondition',
            options={'verbose_name': 'Terms and Conditions', 'verbose_name_plural': 'Terms and Conditions'},
        ),
        migrations.AlterField(
            model_name='termandcondition',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
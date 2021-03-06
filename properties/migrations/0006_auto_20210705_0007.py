# Generated by Django 3.1.1 on 2021-07-05 00:07

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0005_property_commune'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='coordinates',
        ),
        migrations.AddField(
            model_name='property',
            name='coordinate1',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), default=[1, 1], size=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='coordinate2',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), default=[1, 1], size=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='coordinate3',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), default=[1, 1], size=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='coordinate4',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), default=[1, 1], size=2),
            preserve_default=False,
        ),
    ]

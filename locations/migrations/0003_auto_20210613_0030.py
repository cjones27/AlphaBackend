# Generated by Django 3.1.1 on 2021-06-13 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_commune_region_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commune',
            old_name='region_id',
            new_name='region',
        ),
    ]

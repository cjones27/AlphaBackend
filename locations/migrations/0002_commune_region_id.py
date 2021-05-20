# Generated by Django 3.1.1 on 2021-05-13 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commune',
            name='region_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='locations.region'),
            preserve_default=False,
        ),
    ]
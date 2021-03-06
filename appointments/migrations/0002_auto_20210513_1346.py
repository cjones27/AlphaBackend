# Generated by Django 3.1.1 on 2021-05-13 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_is_admin'),
        ('properties', '0002_property_user'),
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='property',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='properties.property'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.user'),
            preserve_default=False,
        ),
    ]

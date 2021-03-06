# Generated by Django 3.1.1 on 2021-05-30 00:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_is_admin'),
        ('communications', '0003_auto_20210513_1420'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='property_id',
            new_name='property',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='sent_by_id',
            new_name='sent_by',
        ),
        migrations.RenameField(
            model_name='notification',
            old_name='property_id',
            new_name='property',
        ),
        migrations.RenameField(
            model_name='notification',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='message',
            name='received_by_id',
        ),
        migrations.AddField(
            model_name='message',
            name='sent_to',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sent_to', to='users.user'),
            preserve_default=False,
        ),
    ]

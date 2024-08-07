# Generated by Django 5.0.7 on 2024-07-25 09:32

import devices.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='device',
            name='description',
        ),
        migrations.AddField(
            model_name='device',
            name='device_id',
            field=models.CharField(default=devices.models.generate_device_id, max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

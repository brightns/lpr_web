# Generated by Django 3.1.4 on 2021-01-05 06:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20201228_1841'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='date_time',
            new_name='update_date_time',
        ),
        migrations.AddField(
            model_name='record',
            name='create_date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

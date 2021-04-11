# Generated by Django 2.2.5 on 2021-04-11 14:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0004_bookedday'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookedday',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookedday',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

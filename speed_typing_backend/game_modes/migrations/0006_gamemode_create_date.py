# Generated by Django 4.2.4 on 2023-08-23 14:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('game_modes', '0005_fixture'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamemode',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

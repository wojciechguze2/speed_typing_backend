# Generated by Django 4.2.4 on 2023-08-23 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_modes', '0002_fixture'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamemode',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]

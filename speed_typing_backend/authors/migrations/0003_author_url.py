# Generated by Django 4.2.4 on 2023-08-21 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0002_fixture'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='url',
            field=models.URLField(null=True),
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-24 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globals', '0002_fixtures'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaticPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=127)),
                ('title', models.CharField(max_length=127)),
                ('content', models.TextField(max_length=255)),
            ],
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-22 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expected_texts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expectedtext',
            name='original_text',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='expected_texts.expectedtext'),
        ),
    ]

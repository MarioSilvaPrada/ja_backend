# Generated by Django 3.2 on 2022-01-23 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_settings_company_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='está ativo'),
        ),
    ]

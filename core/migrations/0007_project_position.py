# Generated by Django 3.2 on 2021-11-14 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20211112_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='position',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
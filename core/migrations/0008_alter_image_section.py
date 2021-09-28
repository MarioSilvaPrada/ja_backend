# Generated by Django 3.2 on 2021-09-22 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_projectsection_section_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='section', to='core.projectsection'),
        ),
    ]
# Generated by Django 3.2.9 on 2021-12-17 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CS_Back', '0002_notes_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
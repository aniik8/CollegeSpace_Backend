# Generated by Django 3.1.5 on 2021-12-21 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CS_QuA', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]

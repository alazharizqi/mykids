# Generated by Django 3.2.4 on 2021-10-27 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akta', '0006_akta_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='akta',
            name='slug',
            field=models.SlugField(blank=True, editable=False),
        ),
    ]

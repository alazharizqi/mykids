# Generated by Django 3.2.4 on 2021-10-26 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akta', '0002_auto_20211026_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='akta',
            name='nik_anak',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='akta',
            name='nomor_kk',
            field=models.CharField(max_length=250),
        ),
    ]

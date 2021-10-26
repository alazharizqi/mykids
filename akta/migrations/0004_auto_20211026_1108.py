# Generated by Django 3.2.4 on 2021-10-26 04:08

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akta', '0003_auto_20211026_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='akta',
            name='akta_nikah',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='akta',
            name='kk',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='akta',
            name='ktp_ayah',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='akta',
            name='ktp_ibu',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='akta',
            name='ktp_saksi',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='akta',
            name='nama_ayah',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='akta',
            name='nama_ibu',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='akta',
            name='nama_saksi',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='akta',
            name='nik_ayah',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='akta',
            name='nik_ibu',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='akta',
            name='nik_saksi',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='akta',
            name='surat_bukti_kelahiran',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='akta',
            name='surat_pengantar_kelahiran',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='jenis_kelamin',
            field=models.CharField(choices=[('Pria', 'Pria'), ('Wanita', 'Wanita')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='nama_anak',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='nik_anak',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='nomor_kk',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='tempat_lahir',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='tgl_lahir',
            field=models.DateField(null=True),
        ),
    ]

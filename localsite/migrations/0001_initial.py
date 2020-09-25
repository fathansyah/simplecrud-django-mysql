# Generated by Django 3.0.7 on 2020-06-22 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nama')),
                ('nik', models.CharField(blank=True, max_length=16, null=True, verbose_name='Nomor Induk Kependudukan')),
                ('ponsel', models.CharField(blank=True, max_length=15, null=True, verbose_name='Nomor HP')),
                ('email', models.CharField(blank=True, max_length=30, null=True, verbose_name='Email')),
                ('alamat', models.CharField(blank=True, max_length=50, null=True, verbose_name='Alamat Sesuai KTP')),
                ('password', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
    ]

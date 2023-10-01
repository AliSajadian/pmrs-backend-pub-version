# Generated by Django 3.2.19 on 2023-09-18 19:04

import django.core.files.storage
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects_files', '0003_alter_hsereportdox_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hsereportdox',
            name='date',
            field=models.DateField(blank=True, db_column='Date', default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='hsereportdox',
            name='file',
            field=models.FileField(db_column='File', null=True, storage=django.core.files.storage.FileSystemStorage(location='D:\\projects\\cost_control\\Pmrs_Files\\Hse_Reports'), unique=True, upload_to=''),
        ),
    ]

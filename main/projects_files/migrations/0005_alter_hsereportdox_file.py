# Generated by Django 3.2.19 on 2023-09-21 02:38

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_files', '0004_auto_20230918_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hsereportdox',
            name='file',
            field=models.FileField(db_column='File', null=True, storage=django.core.files.storage.FileSystemStorage(location='D:\\projects\\cost_control\\Pmrs_Files\\Hse_Reports'), unique=True, upload_to=django.core.files.storage.FileSystemStorage(location='D:\\projects\\cost_control\\Pmrs_Files\\Hse_Reports')),
        ),
    ]

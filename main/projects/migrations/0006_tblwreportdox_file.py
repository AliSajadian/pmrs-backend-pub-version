# Generated by Django 3.2.19 on 2023-09-13 10:49

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_tbljcontractreportdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='tblwreportdox',
            name='file',
            field=models.FileField(db_column='File', null=True, storage=django.core.files.storage.FileSystemStorage(location='../../../files/reportDox'), upload_to=''),
        ),
    ]

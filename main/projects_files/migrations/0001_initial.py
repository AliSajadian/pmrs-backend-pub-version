# Generated by Django 3.2.19 on 2023-09-15 19:19

import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contracts', '0013_alter_tbladdendum_addendumamountdate'),
        ('projects', '0008_alter_tblwreportdox_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='HseReportDox',
            fields=[
                ('hsereportdoxid', models.AutoField(db_column='HseReportDoxID', primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True, db_column='Date', null=True)),
                ('description', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Description', max_length=250)),
                ('file', models.FileField(db_column='File', null=True, storage=django.core.files.storage.FileSystemStorage(location='D:/projects/cost_control/files/projectsDox/hseDox'), upload_to='')),
                ('active', models.BooleanField(blank=True, db_column='Active', null=True)),
                ('contractid', models.ForeignKey(db_column='ContractID', on_delete=django.db.models.deletion.PROTECT, related_name='Contract_HseReportDox', to='contracts.tblcontract')),
                ('dateid', models.ForeignKey(db_column='DateID', on_delete=django.db.models.deletion.PROTECT, related_name='ReportDate_HseReportDox', to='projects.tblwreportdate')),
            ],
            options={
                'db_table': 'tblw_HseReportDox',
            },
        ),
    ]
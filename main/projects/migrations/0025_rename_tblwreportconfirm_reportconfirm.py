# Generated by Django 3.2.19 on 2023-09-26 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0017_alter_tbladdendum_addendumamountdate'),
        ('projects', '0024_rename_tblwprojectpersonel_projectpersonnel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TblwReportconfirm',
            new_name='ReportConfirm',
        ),
    ]

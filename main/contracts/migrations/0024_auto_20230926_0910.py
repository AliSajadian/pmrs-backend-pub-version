# Generated by Django 3.2.19 on 2023-09-26 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0023_auto_20230926_0905'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TblJcontractcostcenter',
            new_name='ContractCostCenter',
        ),
        migrations.RenameModel(
            old_name='TblFinancialdocuments',
            new_name='FinancialDocuments',
        ),
        migrations.RenameModel(
            old_name='TblGrant',
            new_name='Grant',
        ),
        migrations.RenameModel(
            old_name='TblOverheadgroup',
            new_name='OverheadGroup',
        ),
        migrations.RenameModel(
            old_name='TblOverheaditem',
            new_name='OverheadItem',
        ),
        migrations.RenameModel(
            old_name='TblSchedule',
            new_name='Schedule',
        ),
        migrations.RenameModel(
            old_name='TblSchedulebackup',
            new_name='ScheduleBackup',
        ),
        migrations.RenameModel(
            old_name='TblSchedulecellarchive',
            new_name='ScheduleCellArchive',
        ),
    ]

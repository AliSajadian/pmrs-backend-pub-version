# Generated by Django 3.2.19 on 2023-09-26 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0019_rename_tblcompany_company'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TblPersonel',
            new_name='Personel',
        ),
        migrations.RenameModel(
            old_name='TblPersoneltype',
            new_name='Personeltype',
        ),
    ]

# Generated by Django 3.2.19 on 2023-09-26 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0017_alter_tbladdendum_addendumamountdate'),
        ('projects', '0027_auto_20230926_0732'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TblwWorkvolume',
            new_name='WorkVolume',
        ),
    ]

# Generated by Django 3.2.19 on 2023-09-26 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20230828_0051'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TblUser',
            new_name='User',
        ),
        migrations.RenameModel(
            old_name='TblUserlogin',
            new_name='Userlogin',
        ),
    ]

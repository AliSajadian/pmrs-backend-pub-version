# Generated by Django 3.2.19 on 2023-08-14 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_rename_all_projects_w_pmrsuser_all_projects_rw'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tbljuserrole',
            options={'verbose_name': 'User_Contract_Role', 'verbose_name_plural': 'User_Contracts_Roles'},
        ),
    ]

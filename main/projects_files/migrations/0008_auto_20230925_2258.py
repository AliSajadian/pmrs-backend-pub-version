# Generated by Django 3.2.19 on 2023-09-25 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects_files', '0007_approvedinvoicedox_contractordox_projectdox_projectmonthlydox'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contractordox',
            name='active',
        ),
        migrations.RemoveField(
            model_name='contractordox',
            name='dateid',
        ),
    ]
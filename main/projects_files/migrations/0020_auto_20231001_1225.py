# Generated by Django 3.2.19 on 2023-10-01 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_files', '0019_alter_zoneimage_img1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zoneimage',
            name='img2',
            field=models.ImageField(blank=True, db_column='Img2', null=True, unique=True, upload_to='zone_images'),
        ),
        migrations.AlterField(
            model_name='zoneimage',
            name='img3',
            field=models.ImageField(blank=True, db_column='Img3', null=True, unique=True, upload_to='zone_images'),
        ),
    ]

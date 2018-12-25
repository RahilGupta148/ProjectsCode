# Generated by Django 2.1.1 on 2018-12-21 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0007_auto_20181221_2121'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.AlterField(
            model_name='document',
            name='description',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='documents/'),
        ),
    ]

# Generated by Django 2.1.1 on 2018-12-21 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0008_auto_20181221_2124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='document',
            new_name='vidimage',
        ),
    ]

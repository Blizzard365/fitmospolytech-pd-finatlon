# Generated by Django 4.0.5 on 2022-06-24 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_userprofile_delete_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='firstname',
            new_name='firstName',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='lastName',
            new_name='lastname',
        ),
    ]
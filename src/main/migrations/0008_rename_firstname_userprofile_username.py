# Generated by Django 4.0.5 on 2022-06-24 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_userprofile_classnumber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='firstName',
            new_name='username',
        ),
    ]
# Generated by Django 4.0.5 on 2022-06-22 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_classnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='classNumber',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.classnumber'),
        ),
    ]

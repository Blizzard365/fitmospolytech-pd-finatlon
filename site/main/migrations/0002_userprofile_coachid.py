# Generated by Django 4.0.5 on 2022-06-16 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='coachId',
            field=models.IntegerField(default=1, verbose_name='Выберите сопровождающего Вас тренера'),
            preserve_default=False,
        ),
    ]

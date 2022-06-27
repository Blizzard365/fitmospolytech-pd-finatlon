# Generated by Django 4.0.5 on 2022-06-24 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_firstname_userprofile_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sureName', models.CharField(blank=True, max_length=255, verbose_name='Отчество')),
                ('mobile', models.IntegerField(verbose_name='Телефон')),
                ('email', models.EmailField(max_length=255, verbose_name='Email Address')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('region', models.CharField(max_length=255, verbose_name='Регион / Субъект')),
                ('city', models.CharField(max_length=255, verbose_name='Населённый пункт')),
                ('pochtIndex', models.IntegerField(blank=True, verbose_name='Почтовый индекс')),
                ('street', models.CharField(blank=True, max_length=255, verbose_name='Улица')),
                ('houseNumber', models.CharField(blank=True, max_length=10, verbose_name='Номер дома')),
                ('parent', models.CharField(blank=True, max_length=255, verbose_name='ФИО родителя опекуна')),
                ('parentNumber', models.IntegerField(blank=True, verbose_name='Телефон родителя опекуна')),
                ('parentEmail', models.EmailField(blank=True, max_length=255, verbose_name='Email родителя опекуна')),
                ('obrOrgName', models.CharField(max_length=500, verbose_name='Полное наименование образовательной организации')),
                ('obrOrgAdres', models.CharField(blank=True, max_length=500, verbose_name='Адрес (образовательной организации)')),
                ('obrOrgIndex', models.IntegerField(blank=True, verbose_name='Индекс (образовательной организации)')),
                ('obrOrgPhone', models.IntegerField(blank=True, verbose_name='Телефон (образовательной организации)')),
                ('obrOrgEmail', models.EmailField(blank=True, max_length=255, verbose_name='E-mail (образовательной организации)')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('soglasie', models.BooleanField(default=False, verbose_name='Согласие на обработку персональных данных согласно ФЗ-152')),
                ('classNumber', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.classnumber')),
                ('coach', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.coach')),
                ('federalOkrug', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.federalokrug')),
            ],
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]

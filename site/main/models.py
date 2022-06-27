from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(models.Model):
    #coachId = models.IntegerField('Id сопровождающего тренера')
    coach = models.ForeignKey('Coach', on_delete=models.PROTECT, null=True)
    firstname = models.CharField('Имя', max_length=255)
    lastname = models.CharField('Фамилия', max_length=255)
    surename = models.CharField('Отчество', blank=True, max_length=255)
    classNumber = models.ForeignKey('ClassNumber', on_delete=models.PROTECT, null=True)
    mobile = models.IntegerField('Телефон')
    email = models.EmailField('Email Address', max_length=255)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)

    #federalOkrugId = models.IntegerField('Федеральный округ', blank=True)
    federalOkrug = models.ForeignKey('FederalOkrug', on_delete=models.PROTECT, null=True)
    region = models.CharField('Регион / Субъект', max_length=255)
    city = models.CharField('Населённый пункт', max_length=255)
    pochtIndex = models.IntegerField('Почтовый индекс', blank=True)
    street = models.CharField('Улица', max_length=255, blank=True)
    houseNumber = models.CharField('Номер дома', blank=True, max_length=10)

    parent = models.CharField('ФИО родителя опекуна', max_length=255, blank=True)
    parentNumber = models.IntegerField('Телефон родителя опекуна', blank=True)
    parentEmail = models.EmailField('Email родителя опекуна', max_length=255, blank=True)

    obrOrgName = models.CharField('Полное наименование образовательной организации', max_length=500)
    obrOrgAdres = models.CharField('Адрес (образовательной организации)', blank=True, max_length=500)
    obrOrgIndex = models.IntegerField('Индекс (образовательной организации)', blank=True)
    obrOrgPhone = models.IntegerField('Телефон (образовательной организации)', blank=True)
    obrOrgEmail = models.EmailField('E-mail (образовательной организации)', max_length=255, blank=True)

    password = models.CharField('Пароль', max_length=255)
    time_create = models.DateTimeField(auto_now_add=True) # Время для отслеживания сколько времени участник находиться в системе
    soglasie = models.BooleanField('Согласие на обработку персональных данных согласно ФЗ-152', default=False)


    def __str__(self):
        return self.lastName + " " + " " + self.firstName

    # def __str__(self):
    #     return 'Profile for user {}'.format(self.user.username)


class Coach(models.Model):
    name = models.CharField(max_length=100, db_index=True)


    def __str__(self):
        return self.name


class FederalOkrug(models.Model):
    name = models.CharField(max_length=150, db_index=True)


    def __str__(self):
        return self.name


class ClassNumber(models.Model):
    name = models.CharField(max_length=150, db_index=True)


    def __str__(self):
        return self.name
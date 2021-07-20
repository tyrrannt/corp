from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Country(models.Model):
    name_en = models.CharField(verbose_name='Наименование на английском', max_length=100)
    name_ru = models.CharField(verbose_name='Наименование', max_length=100)

    def __str__(self):
        return self.name_en


class City(models.Model):
    country = models.ForeignKey(Country, verbose_name='Страна', on_delete=models.PROTECT)
    name_en = models.CharField(verbose_name='Наименование на английском', max_length=100)
    name_ru = models.CharField(verbose_name='Наименование', max_length=100)

    def __str__(self):
        return self.name_en


class Street(models.Model):
    city = models.ForeignKey(City, verbose_name='Город', on_delete=models.PROTECT)
    name = models.CharField(verbose_name='Наименование', max_length=100)

    def __str__(self):
        return self.name


class Address(models.Model):
    country = models.ForeignKey(Country, verbose_name='Страна', on_delete=models.PROTECT, null=True, blank=True)
    city = models.ForeignKey(City, verbose_name='Город', on_delete=models.PROTECT, null=True, blank=True)
    street = models.ForeignKey(Street, verbose_name='Улица', on_delete=models.PROTECT, null=True, blank=True)
    house = models.CharField(verbose_name='Дом', max_length=10, blank=True)
    apartment = models.CharField(verbose_name='Квартира', max_length=10, blank=True)
    room = models.CharField(verbose_name='Комната', max_length=10, blank=True)


class CorpUserAccess(models.Model):
    level = models.IntegerField(verbose_name='Уровень доступа')
    description = models.CharField(verbose_name='Описание', max_length=255, blank=True)

    def __str__(self):
        return str(self.level)


class CorpUserProfile(models.Model):
    phone = models.CharField(verbose_name='Личный номер телефона', max_length=15, blank=True)
    phone_corp = models.CharField(verbose_name='Корпоративный номер телефона', max_length=15, blank=True)
    phone_internal = models.CharField(verbose_name='Внутренний номер', max_length=3, blank=True)
    email_personal = models.EmailField(verbose_name='E-mail')
    address = models.ForeignKey(Address, verbose_name='Адрес', on_delete=models.SET_NULL, null=True)
    access_right = models.ForeignKey(CorpUserAccess, verbose_name='Права доступа', on_delete=models.SET_NULL, null=True)


class CorpUser(AbstractUser):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'

    GENDERS = (
        (OTHER, 'другой'),
        (MALE, 'мужской'),
        (FEMALE, 'женский'),
    )


    surname = models.CharField(verbose_name='Отчество', max_length=30, default='', blank=True)
    avatar = models.ImageField(verbose_name='Фотография', upload_to='media', blank=True)
    birthday = models.DateField(verbose_name='Дата рождения', null=True)
    gender = models.CharField(verbose_name='Пол', max_length=1, choices=GENDERS, default=OTHER)
    user_profile = models.ForeignKey(CorpUserProfile, verbose_name='Профиль пользователя', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.surname}"

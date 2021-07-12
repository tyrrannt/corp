from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


# Register your models here.
class CustomUserAdmin(UserAdmin):
    """
    Расширяем модель UserAdmin
    fieldsets: исходный набор полей формы
    *UserAdmin.fieldsets: добавляем расширенный набор полей формы,
        тип: кортеж содержащий ('заголовок группы по вашему выбору', {словарь c новыми полями})
    """
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Данные для активации',
            {
                'fields': (
                    'avatar', 'surname',
                ),
            },
        ),
        (
            'Профиль',
            {
                'fields': (
                    'birthday', 'gender', 'user_profile',
                ),
            },
        ),
    )


admin.site.register(CorpUser, CustomUserAdmin)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Street)
admin.site.register(Address)
admin.site.register(CorpUserAccess)
admin.site.register(CorpUserProfile)

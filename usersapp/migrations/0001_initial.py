# Generated by Django 3.2.5 on 2021-07-20 11:13

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house', models.CharField(blank=True, max_length=10, verbose_name='Дом')),
                ('apartment', models.CharField(blank=True, max_length=10, verbose_name='Квартира')),
                ('room', models.CharField(blank=True, max_length=10, verbose_name='Комната')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=100, verbose_name='Наименование на английском')),
                ('name_ru', models.CharField(max_length=100, verbose_name='Наименование')),
            ],
        ),
        migrations.CreateModel(
            name='CorpUserAccess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(verbose_name='Уровень доступа')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=100, verbose_name='Наименование на английском')),
                ('name_ru', models.CharField(max_length=100, verbose_name='Наименование')),
            ],
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='usersapp.city', verbose_name='Город')),
            ],
        ),
        migrations.CreateModel(
            name='CorpUserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=15, verbose_name='Личный номер телефона')),
                ('phone_corp', models.CharField(blank=True, max_length=15, verbose_name='Корпоративный номер телефона')),
                ('phone_internal', models.CharField(blank=True, max_length=3, verbose_name='Внутренний номер')),
                ('email_personal', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('access_right', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='usersapp.corpuseraccess', verbose_name='Права доступа')),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='usersapp.address', verbose_name='Адрес')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='usersapp.country', verbose_name='Страна'),
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='usersapp.city', verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='address',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='usersapp.country', verbose_name='Страна'),
        ),
        migrations.AddField(
            model_name='address',
            name='street',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='usersapp.street', verbose_name='Улица'),
        ),
        migrations.CreateModel(
            name='CorpUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('surname', models.CharField(blank=True, default='', max_length=30, verbose_name='Отчество')),
                ('avatar', models.ImageField(blank=True, upload_to='media', verbose_name='Фотография')),
                ('birthday', models.DateField(null=True, verbose_name='Дата рождения')),
                ('gender', models.CharField(choices=[('O', 'другой'), ('M', 'мужской'), ('F', 'женский')], default='O', max_length=1, verbose_name='Пол')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
                ('user_profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='usersapp.corpuserprofile', verbose_name='Профиль пользователя')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]

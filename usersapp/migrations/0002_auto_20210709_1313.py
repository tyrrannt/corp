# Generated by Django 3.2.5 on 2021-07-09 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usersapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='usersapp.city', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='usersapp.country', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='usersapp.street', verbose_name=''),
        ),
    ]

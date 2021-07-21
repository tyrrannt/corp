# Generated by Django 3.2.5 on 2021-07-21 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usersapp', '0002_auto_20210720_1340'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Название подразделения')),
            ],
        ),
        migrations.AddField(
            model_name='corpuser',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='usersapp.department', verbose_name='Подразделение'),
        ),
    ]

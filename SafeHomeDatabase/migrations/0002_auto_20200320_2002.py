# Generated by Django 3.0.4 on 2020-03-20 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SafeHomeDatabase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devices',
            name='address',
            field=models.CharField(max_length=50, verbose_name='Stream Location'),
        ),
        migrations.AlterField(
            model_name='devices',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Device Id'),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(max_length=50, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=50, verbose_name='Password'),
        ),
    ]

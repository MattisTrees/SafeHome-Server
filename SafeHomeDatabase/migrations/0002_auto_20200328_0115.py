# Generated by Django 3.0.4 on 2020-03-28 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SafeHomeDatabase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owns',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='SafeHomeDatabase.Users'),
        ),
    ]

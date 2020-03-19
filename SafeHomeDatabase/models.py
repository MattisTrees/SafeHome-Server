from django.db import models

# Create your models here.

class Devices(models.Model):
	address = models.CharField('Stream Location', max_length=25)
	name = models.CharField('Device Id', max_length=25)

class Users(models.Model):
	device_owned = models.ForeignKey(Devices, on_delete=models.CASCADE)
	email = models.CharField('Email', max_length=25)
	password = models.CharField('Password', max_length=25)

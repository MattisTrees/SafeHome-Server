from django.db import models

# Create your models here.

class Devices(models.Model):
	address = models.CharField('Stream Location', max_length=60)
	name = models.CharField('Device Id', max_length=60)
	def __str__(self):
		return self.name

class Users(models.Model):
	device_owned = models.ForeignKey(Devices, on_delete=models.CASCADE)
	email = models.CharField('Email', max_length=60)
	password = models.CharField('Password', max_length=60)
	def __str__(self):
		return self.email

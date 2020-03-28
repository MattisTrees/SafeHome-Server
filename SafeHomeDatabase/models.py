from django.db import models

# Create your models here.

class Devices(models.Model):
	address = models.CharField('Stream Location', max_length=60)
	name = models.CharField('Device Id', max_length=60)
	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name

class Users(models.Model):
	email = models.EmailField('Email', max_length=60)
	password = models.CharField('Password', max_length=60)

	class Meta:
		ordering = ['email']

	def __str__(self):
		return self.email

class Owns(models.Model):
	user = models.ForeignKey(Users, null=True, on_delete=models.CASCADE)
	device = models.ForeignKey(Devices, null=True, on_delete=models.CASCADE)

	class Meta:
		ordering = ['user']

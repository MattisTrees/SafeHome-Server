from django.shortcuts import render
from SafeHomeDatabase.models import *
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("Hello, world! Nothing to see here.  You're at the SafeHomeDatabase index.")

def signin(request):
	# Retrieve the GET request value for 'email'
	inputEmail = request.GET.get('email')
	# Retrieve the GET request value for 'password'
	inputPassword = request.GET.get('password')
	# Retrieve the all of the models for 'Users' from the database
	try:
		user = Users.objects.get(email=inputEmail).email
		print(user)
	except:
		return HttpResponse("User not found")
	if inputEmail == user:
		return HttpResponse("User has been found!")
	else:
		return HttpResponse("Receiving this response means there is a problem with the return of 'Users.objects.get(email=inputEmail).email")
	return HttpResponse("Email: " + inputEmail + " Pass: " + inputPassword)


from django.shortcuts import render
from SafeHomeDatabase.models import *
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("Hello, world! Nothing to see here!  You're at the SafeHomeDatabase index.")

def signUp(request):
	inputEmail = request.GET.get('email')
	inputPassword = request.GET.get('password')
        # Check to make sure email is not already registered
	try:
		user = Users.objects.get(email=inputEmail)
	except:
		# Email not found in database, make new Users object and add it to the Database
		newUser = Users(email=inputEmail, password=inputPassword)
		newUser.save()
		return HttpResponse("Registration for  complete")
	return HttpResponse("Email already in use.")

def signIn(request):
	# Retrieve the GET request value for 'email'
	inputEmail = request.GET.get('email')
	# Retrieve the GET request value for 'password'
	inputPassword = request.GET.get('password')
	# Retrieve the all of the models for 'Users' from the database
	try:
		user = Users.objects.get(email=inputEmail)
		print(user)
	except:
		return HttpResponse("Email not found.")
	if inputEmail == user.email:
		if inputPassword == user.password :
			return HttpResponse("You are now logged in!")
		else :
			return HttpResponse("Incorrect Password!")
	else:
		return HttpResponse("Receiving this response means there is a problem with the return of 'Users.objects.get(email=inputEmail).email")

# function to return a list of device names and their feed information
def getDevices(request):
	inputEmail = request.GET.get('email')
	devicesOwned = Owns.objects.filter(user__email=inputEmail).values('device__name', 'device__address')
	returnValue = ""
	for device in devicesOwned:
		returnValue += device['device__name']  + ":" +  device['device__address'] + ", "
	return HttpResponse(returnValue)

def addDevice(request):
	inputEmail = request.GET.get('email')
	deviceId = request.GET.get('device')
	try:
		existingDevice = Devices.objects.get(name=deviceId)
	except:
		return HttpResponse("Device not found")
	try:
		existingUser = Users.objects.get(email=inputEmail)
	except:
		return HttpResponse("Email not in database!")
	new_relationship = Owns(user=existingUser, device=existingDevice)
	new_relationship.save()
	return HttpResponse("Device " + deviceId + " Saved to your account!")

def deleteDevice(request):
	deviceId = request.GET.get('device')
	inputEmail = request.GET.get('email')
	try:
		deviceOwned = Owns.objects.filter(user__email=inputEmail, device__name=deviceId)
	except:
		return HttpResponse("Device not found!")
	try:
		deviceOwned.delete()
	except:
		return HttpResponse("Could not delete device!")
	return HttpResponse("Device successfully deleted")

def changeDeviceName(request):
	return HttpResponse("This method will be added in a later sprint")

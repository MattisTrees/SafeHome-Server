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
		return HttpResponse("Registration for " + inputEmail + " complete")
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
	devicesOwned = Owns.objects.filter(user__email=inputEmail).values('device__name', 'device__address', 'device__id')
	returnValue = ""
	for device in devicesOwned:
		returnValue += str(device['device__id']) + "-" + device['device__name']  + "-" +  device['device__address'] + ", "
	return HttpResponse(returnValue)

def addDevice(request):
	inputEmail = request.GET.get('email')
	deviceId = request.GET.get('deviceId')
	try:
		existingDevice = Devices.objects.get(id=deviceId)
	except:
		return HttpResponse("Device not found")
	try:
		existingUser = Users.objects.get(email=inputEmail)
	except:
		return HttpResponse("Email not in database!")
	new_relationship = Owns(user=existingUser, device=existingDevice)
	# Check to see if relationship already exists
	try:
		alreadyOwns = Owns.objects.get(user=existingUser, device=existingDevice)
	except:
		# Relattionship is not yet in the table
		new_relationship.save()
		return HttpResponse("Device " + deviceId + " Saved to your account!")
	return HttpResponse("This device is already registered with your account!")

# This function has a minor bug that doesn't check if the device requested to be deleted actually exists on the server.
# It shouldn't matter much because the user doesn't manually enter the device name, it's taken from local variables
# in the SafeHome App.
def deleteDevice(request):
	deviceId = request.GET.get('deviceId')
	inputEmail = request.GET.get('email')
	deviceOwned = Owns.objects.filter(user__email=inputEmail, device__id=deviceId)
	if deviceOwned.count() == 1:
		try:
			deviceOwned.delete()
		except:
			return HttpResponse("Could not delete device!")
		return HttpResponse("Device successfully deleted!")
	else:
		if deviceOwned.count() >= 1:
			return HttpResponse ("There might be more than one entry in the table for this relationship!!!")
		else:
			return HttpResponse("Device not associated with this account!")
		return HttpResponse("There is some mistake")

def changeDeviceName(request):
	deviceId = request.GET.get('deviceId')
	newName = request.GET.get('deviceName')
	device = Devices.objects.get(id=deviceId)
	oldName = device.name
	device.name = newName
	device.save()
	return HttpResponse(oldName + " has been renamed to " + device.name)

def createDevice(request):
	newDevice = Devices(name=request.GET.get('name'), address=request.GET.get('address'))
	newDevice.save()
	return HttpResponse("Device created succesfully with name=" + newDevice.name + " address=" + newDevice.address)

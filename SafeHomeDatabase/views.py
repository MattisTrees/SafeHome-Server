from django.shortcuts import render
from SafeHomeDatabase.models import Users, Devices
from django.http import HttpResponse

# Create your views here.

def index(request):
	user = Users.objects.get(id=1)
	print(user.email)
	return HttpResponse("Hello, world. The User you were looking for is " + str(user.email) + " with password " + str(user.password) + " with access to " + str(user.device_owned))

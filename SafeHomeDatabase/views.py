from django.shortcuts import render
from SafeHomeDatabase.models import Users, Devices
from django.http import HttpResponse

# Create your views here.

def index(request):
	user = request.GET.get('username')
	print(user)
	return HttpResponse("Hello, world. The user you requested is: " + str(user))

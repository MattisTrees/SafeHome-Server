from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('signIn/', views.signIn, name='signIn'),
	path('getDevices/', views.getDevices, name='getDevices'),
	path('signUp/', views.signUp, name='signUp'),
	path('addDevice/', views.addDevice, name='addDevice'),
]

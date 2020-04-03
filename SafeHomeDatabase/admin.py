
from django.contrib import admin
from .models import *
# Register your models here.

class DeviceAdmin(admin.ModelAdmin):
	readonly_fields = ('id',)

admin.site.register(Users)
admin.site.register(Devices, DeviceAdmin)
admin.site.register(Owns)

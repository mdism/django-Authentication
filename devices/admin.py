from django.contrib import admin
from .models import Device

class DeviceAdmin(admin.ModelAdmin):
    readonly_fields = ('device_id', 'name', 'brand','units')

admin.site.register(Device, DeviceAdmin)

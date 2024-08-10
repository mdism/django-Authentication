from django.contrib import admin
from .models import Device

class DeviceAdmin(admin.ModelAdmin):
    readonly_fields = ('device_id', 'name', 'location','description')

admin.site.register(Device, DeviceAdmin)

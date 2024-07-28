from django import forms
from .models import Device

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'brand','units']
        widgets = {
            'device_id': forms.TextInput(attrs={'readonly': 'readonly'}),
            
        }

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Device
from .influxdb_utils import write_data, query_data
from .forms import DeviceForm

@login_required
def device_list(request):
    # username=request.user.username
    devices = Device.objects.filter(user=request.user)
    return render(request, 'devices/device_list.html', {'devices': devices})

@login_required
def add_device(request):
    if request.method == 'POST':    
        form = DeviceForm(request.POST)
        if form.is_valid():
            device = form.save(commit=False)
            device.user = request.user
            device.save()
            return redirect('device_list')
    else:
        form = DeviceForm()
    return render(request, 'devices/device_form.html', {'form': form})

@login_required
def edit_device(request, pk):
    device = get_object_or_404(Device, pk=pk, user=request.user)
    if request.method == 'POST':
        form = DeviceForm(request.POST, instance=device)
        if form.is_valid():
            form.save()
            return redirect('device_list')
    else:
        form = DeviceForm(instance=device)
    return render(request, 'devices/device_form.html', {'form': form})

@login_required
def delete_device(request, pk):
    device = get_object_or_404(Device, pk=pk, user=request.user)
    if request.method == 'POST':
        device.delete()
        return redirect('device_list')
    return render(request, 'devices/device_confirm_delete.html', {'device': device})


def write_device_data(request):
    if request.method == 'POST':
        device_id = request.POST['device_id']
        data = {
            'temperature': float(request.POST['temperature']),
            'humidity': float(request.POST['humidity']),
        }
        write_data(device_id, data)
        return render(request, 'data_written.html')

def show_device_data(request):
    query = 'from(bucket:"iot_data") |> range(start: -1h) |> filter(fn: (r) => r._measurement == "device_data")'
    results = query_data(query)
    return render(request, 'device_data.html', {'results': results})
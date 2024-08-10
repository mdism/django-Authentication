import uuid
from django.db import models
from django.contrib.auth.models import User

def generate_device_id():
    return uuid.uuid4().hex

class Device(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    device_id = models.CharField(max_length=32, unique=True, default=generate_device_id)

    def __str__(self):
        return self.name

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Used_stuff(models.Model):
    name = models.CharField(max_length=225)
    selling_price = models.FloatField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.CharField(max_length=225)
    location = models.CharField(max_length=225)
    category = models.IntegerField() #0->cloth
    source = models.IntegerField()
    def __str__(self):
        return str(self.id)


from django.db import models
from django.contrib.auth.models import User as BaseUser


class Store(models.Model):
    name = models.CharField(max_length=100)
    logo_url = models.URLField()
    website_url = models.URLField()

    def __str__(self):
        return self.name

class PricePerKg(models.Model):
    price = models.FloatField()

class CustomUser(models.Model):
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE)
    destinationCountry = models.TextField(default="")
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.IntegerField()
    email = models.EmailField()
    unique_address = models.TextField()
    unique_id = models.TextField()
    forward_consolidation = models.BooleanField(default=False)
    
    def __str__(self):
        return self.unique_id

class Notification(models.Model):
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

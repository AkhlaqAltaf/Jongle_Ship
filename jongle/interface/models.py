from django.db import models
from django.contrib.auth.models import User as baseuser

class CustomUser(models.Model):
      user = models.OneToOneField(baseuser, on_delete=models.CASCADE)
      name = models.CharField(max_length=100)
      address = models.TextField()
      phone = models.IntegerField()
      email = models.EmailField()
      unique_address = models.TextField()
      unique_id = models.TextField()
      
    
      def __str__(self):
        return self.unique_id
    

class Store(models.Model):
    name = models.CharField(max_length=100)
    logo_url = models.URLField()
    website_url = models.URLField()    

    def __str__(self):
        return self.name
    

class Profile(models.Model):
    
    user = models.ForeignKey(baseuser, on_delete=models.CASCADE)
    package_image = models.ImageField(upload_to='package_images', blank=True, null=True)
    package_dimensions = models.CharField(max_length=100, blank=True, null=True)
    package_weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    package_name = models.TextField(max_length=200, blank=True, null=True)
    package_price = models.IntegerField(blank=True, null=True)
    package_description = models.TextField(blank=True, null=True)
    # Other profile fields

    def __str__(self):
        return self.user.username    
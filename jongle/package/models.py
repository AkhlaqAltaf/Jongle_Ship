from django.db import models
from django.contrib.auth.models import User as baseuser
# Create your models here.




class Profile(models.Model):
    user = models.ForeignKey(baseuser, on_delete=models.CASCADE, related_name='profiles')
    tracking_number = models.CharField(max_length=50, blank=True, null=True)
    destinationCountry= models.TextField(default='')
    package_image = models.ImageField(upload_to='package_images', blank=True, null=True)
    package_dimensions = models.CharField(max_length=100, blank=True, null=True)
    package_weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    package_name = models.TextField(max_length=200, blank=True, null=True)
    package_price = models.IntegerField(blank=True, null=True)
    package_description = models.TextField(blank=True, null=True)
    forward_consolidation = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username    
    

class Package(models.Model):
    action_choices = [
        ('forward', 'Forward'),
        ('repackage', 'Repackage'),
        ('consolidate', 'Consolidate'),
        ('no_decision', 'No Decision'),
    ]

  
    selected_action = models.CharField(max_length=20, choices=action_choices, default='no_decision')
    in_progress_packages = models.ManyToManyField(Profile, through='InProgressPackage', related_name='in_progress_packages')
    ready_to_ship_packages = models.ManyToManyField(Profile, through='ReadyToShip', related_name='ready_to_ship_packages')
    warehouse_packages = models.ManyToManyField(Profile, through='WarehousePackage', related_name='warehouse_packages')
           
    
    def __str__(self):
        return f"{self.selected_action}"  
    
class WarehousePackage(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, related_name='warehouse_package', on_delete=models.CASCADE)
    action_required = models.BooleanField(default=False)
    selected_action = models.CharField(max_length=20, choices=Package.action_choices, default='no_decision')

    def __str__(self):
        return f"{self.package} - {self.selected_action}"

      



class InProgressPackage(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, related_name='in_progress', on_delete=models.CASCADE)
    action_required = models.BooleanField(default=False)
    selected_action = models.CharField(max_length=20, choices=Package.action_choices, default='no_decision')

    def __str__(self):
        return f"{self.package} - {self.selected_action}"



class ReadyToShip(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, related_name='ready_to_ship', on_delete=models.CASCADE)
    action_required = models.BooleanField(default=False)
    selected_action = models.CharField(max_length=20, choices=Package.action_choices, default='no_decision')

    def __str__(self):
        return f"{self.package} - {self.selected_action}"




      



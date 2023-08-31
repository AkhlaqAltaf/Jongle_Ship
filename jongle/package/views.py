from django.shortcuts import render
from django.shortcuts import redirect, render 
from interface.models import *
from user.models import *
from interface.models import Store
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from interface.controler import notification_controller as nc

from interface.controler import other_controller as oc
from interface.controler import api_controller as api_c
from interface.controler import email_controller as ec
from .controller import package_controller as pc
from .models import *
class Pages:
    
    def my_packages(request):
        return pc.my_packages(request)
    
    def warehouse(request):

        return pc.warehouse(request)
    
    


    def show_repackage_popup(request, profile_id):

        return pc.show_repackage_popup(request , profile_id)
    

    def process_repackage(request, profile_id):

        return pc.process_repackage(request , profile_id)
    



    def show_forward_popup(request, profile_id):
        profile = Profile.objects.get(id=profile_id)
        packages = profile.related_packages.filter(action_required=True)
        return render(request, 'package/forward_popup.html', {'profile': profile, 'packages': packages})
    


    def process_forward(request, profile_id):
        return pc.process_forward(request , profile_id)
    


    def show_consolidate_popup(request, profile_id):
        profile = Profile.objects.get(id=profile_id)
        packages = profile.related_packages.filter(action_required=True)
        return render(request, 'package/consolidate_popup.html', {'profile': profile, 'packages': packages})



    def process_consolidate(request, profile_id):
        return pc.process_consolidate(request , profile_id)
    


    def process_actions(request):


        return pc.process_actions(request)
    

    @login_required
    def upload_package(request):   
        return pc.upload_package(request)
 

    # Update Consolildation 
    def update_consolidation(request):
            return pc.update_consolidation()


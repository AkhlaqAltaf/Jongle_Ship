from django.shortcuts import render
from django.shortcuts import render 
from interface.models import *
from user.models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, redirect
from user.models import UserProfile
from .models import Package, WarehousePackage
from django.core.mail import send_mail
from django.shortcuts import render, redirect
   
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

    @login_required
    def upload_package(request):
        if request.method == 'POST':
            package_name = request.POST.get('package_name')
            action_required = request.POST.get('action_required')
            user_profile_id = request.POST.get('user_profile_id')
            
            package = Package.objects.create(package_name=package_name)
            user_profile = UserProfile.objects.get(id=user_profile_id)

            warehouse_package = WarehousePackage.objects.create(
                user_profile=user_profile,
                package=package,
                action_required=action_required,
                selected_action=action_required
            )

            return redirect('admin_package_list')
        
        user_profiles = UserProfile.objects.all()
        return render(request, 'admin/upload_package.html', {'user_profiles': user_profiles})

    def send_package(request, package_id):
        if request.method == 'POST':
            package = WarehousePackage.objects.get(id=package_id)
            package.delete()
            send_mail(
                'Your Package is on the Way',
                'Your package has been sent.',
                'jongleship@gmail.com',  # Change to your email address
                [package.user_profile.user.email],
                fail_silently=False,
            )
            return redirect('admin_package_list')

        package = WarehousePackage.objects.get(id=package_id)
        return render(request, 'package/in_warehouse.html', {'package': package})

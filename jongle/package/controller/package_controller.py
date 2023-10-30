from django.http import JsonResponse
from django.contrib.auth.models import User
from django.urls import reverse
from package.models import Profile , WarehousePackage
from django.contrib import messages
from django.shortcuts import render , redirect
from django.template.loader import render_to_string
from interface.controler import email_controller as ec
from interface.controler import other_controller as oc
from interface.controler import api_controller as api_c
from interface.controler import notification_controller as nc



def upload_package(request):
    username = request.GET.get('username')
    countryCode = request.GET.get('destinationCountry')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            user = User.objects.get(username=username)
            package_image = request.FILES.get('packageImage')
            tracking_number = request.POST.get("trackingNumber")
            destination_country = request.POST.get("destinationCountry")
            package_dimensions = request.POST.get('packageDimensions')
            package_weight = request.POST.get('packageWeight')
            package_name = request.POST.get('name')
            package_price = request.POST.get('price')
            package_description = request.POST.get('description')

            # Create the Profile instance
            profile = Profile(user=user, tracking_number=tracking_number, destinationCountry=destination_country,
                              package_image=package_image, package_dimensions=package_dimensions,
                              package_weight=package_weight, package_name=package_name,
                              package_price=package_price, package_description=package_description,
                              forward_consolidation=False)
            profile.save()

            # # Create a corresponding WarehousePackage instance with "Action Required" status
            # warehouse_package = WarehousePackage(profile=profile, package=profile,
            #                                      action_required=True, selected_action='no_decision')
            # warehouse_package.save()

            # Generate barcode image
            # barcode_image_data = oc.generate_barcode(profile)
            context = {
                'profiles': [profile],  # Pass the profile as a list to match the template structure
                'request': request  # Pass the request object for context variable 'request.user'
            }

            # Send email with barcode image
            html_content = render_to_string('interface_templates/package_detail_email.html', context)
            ec.send_package_details_email(user.email, html_content)
            nc.add_package_notification(user, request)

            messages.success(request, f"Package uploaded for user: {user.username}")
        except User.DoesNotExist:
            messages.error(request, "User does not exist.")

    return render(request, 'interface_templates/upload_package.html', {'username': username, 'destinationCountry': countryCode})


def update_consolidation(request):

    if request.method == 'POST':

        consolidation = request.POST.get('consolidation')
        tracking_number =request.POST.get('tracking_number')

        # profile = Profile.objects.filter(tracking_number =tracking_number ).update(farward_consolidation = consolidation)
        profile = Profile.objects.filter(tracking_number=tracking_number).update(forward_consolidation=consolidation)

        messages.success(request , "Update Success")

        return JsonResponse({"update" :consolidation})
    


def package_details(request):

    profiles = Profile.objects.filter(user=request.user)

    if request.user.is_authenticated:

        if profiles.exists():

            print(profiles)
            trackingId=profiles[0].tracking_number

            track_data = api_c.get_tracking_data(trackingId)
            print(track_data)
            context = {
                'profiles': profiles,
                'track_data':track_data
            }


        

            return render(request, 'interface_templates/package_details.html', context)
        else:
            messages.error(request, "No Packages Found ...")
            return render(request, 'interface_templates/package_details.html')
    else:
        messages.info(request, "Please log in to view package details.")
        return redirect('user/login')  # Specify your login URL here

    




def my_packages(request):

    return render(request , 'package/base_packages.html')



def warehouse(request):
    # Get all packages that are in "Action Required" status
    action_required_packages = WarehousePackage.objects.filter(action_required=True)
    
    return render(request, 'package/in_warehouse.html', {'action_required_packages': action_required_packages})




def show_repackage_popup(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    packages = profile.related_packages.filter(action_required=True)
    return render(request, 'package/repackage_popup.html', {'profile': profile, 'packages': packages})

def process_repackage(request, profile_id):
    if request.method == 'POST':
        selected_packages = request.POST.getlist('selected_packages')
        new_package = WarehousePackage.objects.create(profile_id=profile_id, action_required=False, selected_action='repackage')
        new_package.save()
        for package_id in selected_packages:
            package = WarehousePackage.objects.get(id=package_id)
            package.profile = new_package
            package.save()
    return redirect('in_warehouse')



def process_actions(request):
    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith('package_'):
                package_id = int(key.split('_')[1])
                package = WarehousePackage.objects.get(id=package_id)
                package.selected_action = value
                package.action_required = False

                if value == 'forward':
                    # Perform logic for the forward action
                    package.save()
                elif value == 'repackage_forward':
                    # Show the repackage pop-up for the package
                    return redirect('show_repackage_popup', profile_id=package.profile.id)
                elif value == 'consolidate':
                    # Show the consolidate pop-up for the package
                    return redirect('show_consolidate_popup', profile_id=package.profile.id)
                else:
                    package.save()

    return redirect('in_warehouse')


def process_consolidate(request, profile_id):

    if request.method == 'POST':
        selected_packages = request.POST.getlist('selected_packages')
        new_package = WarehousePackage.objects.create(profile_id=profile_id, action_required=False, selected_action='consolidate')
        new_package.save()
        for package_id in selected_packages:
            package = WarehousePackage.objects.get(id=package_id)
            package.profile = new_package
            package.save()
    return redirect('in_warehouse')



def process_forward(request, profile_id):
    if request.method == 'POST':
        selected_packages = request.POST.getlist('selected_packages')
        new_package = WarehousePackage.objects.create(profile_id=profile_id, action_required=False, selected_action='forward')
        new_package.save()
        for package_id in selected_packages:
            package = WarehousePackage.objects.get(id=package_id)
            package.profile = new_package
            package.save()
    return redirect('in_warehouse')
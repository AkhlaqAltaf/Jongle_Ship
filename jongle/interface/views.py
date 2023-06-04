from io import BytesIO
from django.shortcuts import render ,HttpResponse ,redirect
from interface.models import *
from django.contrib import messages
from datetime import datetime
from interface.models import Store
from django.utils.translation import gettext as gt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives

import barcode
from barcode.writer import ImageWriter
from django.http import HttpResponse
from PIL import Image, ImageDraw, ImageFont
import io
import win32print
import tempfile
from django.conf import settings


# Create your views here.


class Pages:


    def home(request):


        return render(request , 'home.html')
    # signup rende 

    def signup(request):

        return render(request,'signup.html')



    def saveauth(request):
       
        if request.method == "POST":

                name = request.POST.get('name')
               


                userauth = authenticate(username = name)
                

                if userauth != None:
                     messages.warning(request, "This User Name is Already Containing....Please Enter Unique Name")
                     
                     return redirect('signup')

                else:

                    address = request.POST.get('address')
                    phone = request.POST.get('phone')
                    email = request.POST.get('email')
                    
                    unique_address = address + str(len(CustomUser.objects.all()))
                    unique_id = name + str(datetime.now())
                    password = request.POST.get('password')

                    # Retrieve or create the User instance
                    user, created = User.objects.get_or_create(username=name , password = password)
                    user.set_password(password)
                    user.save()

                    new_user = CustomUser(user=user, name=name, address=address, phone=phone, email=email, unique_address=unique_address, unique_id=unique_id)
                    new_user.save()
                    messages.success(request, "Successfully Registered.")
                    
                    return redirect('/')


        
#   signin render   

    def signin(request):
        return render(request, 'signin.html')
             

    def signin_auth(request):

        print(request.user.is_anonymous)


        if request.method == 'POST':
             
             username = request.POST.get('username')
             password = request.POST.get('password')

             print(username , password)

             userauth = authenticate(username = username , password = password)
             print(userauth)

             if userauth is not None:
                messages.success(request,"successfully login......")
                login(request,userauth)
                return  redirect ('/')
             else :
                messages.error(request, 'User Name or password wrong......')
                return redirect('signin')


    def store_list(request):
        stores = Store.objects.all()
        return render(request, 'store_list.html', {'stores': stores})
    

    def help(request):
         
         return render(request ,"help.html")
    


    def logout(request):
       
        logout(request)

        return redirect ('signin') 


# Packages Detail Will Show 
    @login_required(login_url='signin')  # Specify your login URL here
    def package_details(request):
        profiles = Profile.objects.filter(user=request.user)

        if request.user.is_authenticated:
            if profiles.exists():
                context = {
                    'profiles': profiles
                }
               

                return render(request, 'package_details.html', context)
            else:
                messages.error(request, "No Packages Found ...")
                return render(request, 'package_details.html')
        else:
            messages.info(request, "Please log in to view package details.")
            return redirect('login')  # Specify your login URL here

        

 


    # @login_required
    # def upload_package(request):
        
    #     if request.user.is_superuser:  # Check if current user is an admin
    #         if request.method == 'POST':
    #             username = request.POST.get('username')
    #             try:
                    
    #                 user = User.objects.get(username=username)
    #                 package_image = request.FILES.get('packageImage')
    #                 package_dimensions = request.POST.get('packageDimensions')
    #                 package_weight = request.POST.get('packageWeight')

    #                 profile = Profile(user=user, package_image=package_image, package_dimensions=package_dimensions,
    #                                 package_weight=package_weight)
    #                 profile.save()
    #                 context = {
    #                 'profiles': [profile],  # Pass the profile as a list to match the template structure
    #                 'request': request  # Pass the request object for context variable 'request.user'
    #             }
                    
    #                 html_content = render_to_string('package_detail_email.html', context)
    #                 Pages.send_package_details_email(user.email, html_content)
    #                 Pages.generate_barcode(request,profile=profile)
    #                 messages.success(request, f"Package uploaded for user: {user.username}")
                    
                   
    #             except User.DoesNotExist:
    #                 messages.error(request, "User does not exist.")
    #         return render(request, 'upload_package.html')
    #     else:
    #         messages.error(request, "You do not have permission to perform this action.")
    #         return redirect('/')
       

    # def send_package_details_email(user_email, html_content):
    #     subject = "Package Details"
    #     from_email = "merndeveloper123@gmail.com"
        
    #     msg = EmailMultiAlternatives(subject, '', from_email, ['akhlaqaltaf4@gmail.com'])
    #     msg.attach_alternative(html_content, "text/html")
        
    #     msg.send() 




  






    def generate_barcode(profile):
        # Retrieve the package details from the profile object
        username = profile.user.username
        email = profile.user.email
        package_dimensions = profile.package_dimensions
        package_weight = profile.package_weight

        # Generate the barcode value using the package details
        barcode_value = f"username : {username}, email : {email},  Dimensions: {package_dimensions}, Weight: {package_weight}"

        # Generate barcode using python-barcode library
        barcode_image = barcode.Code128(barcode_value, writer=ImageWriter())

        # Create a file-like object to store the barcode image
        barcode_file = BytesIO()
        barcode_image.write(barcode_file)
     
        return barcode_file.getvalue()
    



    @login_required
    def upload_package(request):
        username = request.GET.get('username')

        if request.method == 'POST':
            username = request.POST.get('username')
            try:
                user = User.objects.get(username=username)
                package_image = request.FILES.get('packageImage')
                package_dimensions = request.POST.get('packageDimensions')
                package_weight = request.POST.get('packageWeight')
                package_name = request.POST.get('name')
                package_price = request.POST.get('price')
                package_description = request.POST.get('description')
                profile = Profile(user=user, package_image=package_image, package_dimensions=package_dimensions,
                                package_weight=package_weight , package_name =package_name , package_price = package_price , package_description = package_description)
                profile.save()

                # Generate barcode image
                barcode_image_data = Pages.generate_barcode(profile)
                context = {
                    'profiles': [profile],  # Pass the profile as a list to match the template structure
                    'request': request  # Pass the request object for context variable 'request.user'
                }
                # Send email with barcode image
                html_content = render_to_string('package_detail_email.html', context)
                Pages.send_package_details_email(user.email, html_content, barcode_image_data)

                messages.success(request, f"Package uploaded for user: {user.username}")
            except User.DoesNotExist:
                messages.error(request, "User does not exist.")

        return render(request, 'upload_package.html', {'username': username})

    def send_package_details_email(recipient_email, html_content, barcode_image_data):
            # Create an EmailMultiAlternatives object
            email = EmailMultiAlternatives(
                "Package Details",
                "Here are the package details:",
                "jongleship@gmail.com",
                ['merndeveloper123@gmail.com'],
            )

            # Attach the HTML content to the email
            email.attach_alternative(html_content, "text/html")

            # Attach the barcode image to the email
            email.attach("barcode.png", barcode_image_data, "image/png")

            # Send the email
            email.send()



# //////////////////Send Message from  email 

    @login_required
    def send_message(request):
        print("Enter In Defination.........")
       

        
        if request.method == 'POST':
            email =  request.POST.get('email')
            username = request.POST.get('username')
            message = request.POST.get('message')
            subject = request.POST.get('subject')
            send_mail(
                subject,  # Subject
                message,  # Message
                settings.HOST_EMAIL,  # From email address
                [email],  # To email address
                fail_silently=False
            )
            messages.success(request, f"Message sent to user: {username}")
            return redirect('admin:interface_customuser_changelist')
        else:
            username = request.GET.get('username')
            object = CustomUser.objects.get(name= username)
            email_= object.email
            return render(request, 'send_message.html', {'username': username, 'email': email_})
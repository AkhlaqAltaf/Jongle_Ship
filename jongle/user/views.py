from django.shortcuts import render ,redirect
from django_countries import countries
from interface.models import *
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str

from django.conf import settings





# Create your views here.


class Pages:


    # signup render 

    def signup(request):
        
        countries_list = [(code, name) for code, name in countries]

        return render(request,'user_templates/signup.html' ,{'countries_list':countries_list})



#  Save Auth / Register User 

    def saveauth(request):
       
        if request.method == "POST":

                name = request.POST.get('username')
               
                


                userauth = authenticate(username = name)
                

                if userauth != None:
                     messages.warning(request, "This User Name is Already Containing....Please Enter Unique Name")
                     
                     return redirect('/user/signup')

                else:
                    country = request.POST.get('destinationCountry')
                    address = request.POST.get('address')
                    phone = request.POST.get('phone')
                    email = request.POST.get('email')
                    
                    unique_address = address + str(len(CustomUser.objects.all()))
                    unique_id = name + address
                    password = request.POST.get('password')
                    consolidation = request.POST.get('consolidation')
                    # Retrieve or create the User instance
                    try:
                        user, created = User.objects.get_or_create(username=name , password = password)

                        user.set_password(password)

                        user.save()
                    except Exception as e:
                        messages.error(request, e)
                        print("Exception Occur ",e)

                        return redirect('/user/signup')

                
                

                    new_user = CustomUser(user=user,destinationCountry = country ,name=name, address=address, phone=phone, email=email, 
                                          unique_address=unique_address, unique_id=unique_id , forward_consolidation = consolidation)
                    try:
                        new_user.save()


                        messages.success(request, "Successfully Registered.")
                        
                        return Pages.signin_auth(request)

                    except Exception as e:
                        messages.error(request, e)

                        return redirect('/user/signup')
                         
        else :

            return redirect('/user/signup')           


        

#   signin render   

    def signin(request):
        return render(request, 'user_templates/signin.html')





        #    SignIn Authentication
          

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
    





#  Logout User 




    def logout(request):
       
        logout(request)

        return redirect ('/user/signin') 





        








#  Send Package Detail Via Email 



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










# Send Message from  email 

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
            return render(request, 'user_templates/send_message.html', {'username': username, 'email': email_})
        







        # Foragate Password , Enter Email 


     
    def reset_password(request):
        if request.method == 'POST':
            email = request.POST['email']
            custom_user = CustomUser.objects.filter(email=email).first()
    
            if custom_user:
                user = custom_user.user
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                reset_link = request.build_absolute_uri(f'/reset_password/{uid}/{token}/')
                
                Pages.send_password_reset_email(custom_user.email, reset_link)
                messages.success(request, 'An email has been sent with instructions to reset your password.')
                return redirect('user/signin')
            else:
                messages.error(request, 'No user with that email address exists.')
                return redirect('user/reset_password')

        return render(request, 'user_templates/reset_password.html')








# Reset Password Confirmation 



    def reset_password_confirm(request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
            print("User Is does not exit........")

        if user and default_token_generator.check_token(user, token):

            if request.method == 'POST':
                password = request.POST['password']
                user.set_password(password)
                user.save()
                messages.success(request, 'Your password has been reset successfully. Please log in.')
                return redirect('user/signin')
            return render(request, 'user_templates/reset_password_confirm.html')
        else:
            messages.error(request, 'The reset password link is invalid.')
            return redirect('user/signin')
        






    # Send Password To A User

    def send_password_reset_email(email, reset_link):

        subject = 'Reset Your Password'
        message = render_to_string('user_templates/reset_password_email.html', {
            'reset_link': reset_link
        })
        send_mail(subject, message, settings.HOST_EMAIL, [email])







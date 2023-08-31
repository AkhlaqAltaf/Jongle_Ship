
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import redirect, render
from interface.models import CustomUser

from twisted.mail.smtp import sendmail
from django.contrib.auth.decorators import login_required
def send_package_details_email(recipient_email, html_content, barcode_image_data):
        # Create an EmailMultiAlternatives object
        email = EmailMultiAlternatives(
            "Package Details",
            "Here are the package details:",
            "jongleship@gmail.com",
            [recipient_email],
        )

        # Attach the HTML content to the email
        email.attach_alternative(html_content, "text/html")

        # Attach the barcode image to the email
        email.attach("barcode.png", barcode_image_data, "image/png")

        # Send the email
        email.send()




@login_required
def send_message(request):
    print("Enter In Defination.........")
    

    
    if request.method == 'POST':
        email =  request.POST.get('email')
        username = request.POST.get('username')
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        sendmail(
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
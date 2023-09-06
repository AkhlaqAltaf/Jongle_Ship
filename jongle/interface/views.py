from django.shortcuts import render 
from interface.models import *
from user.models import *
from interface.models import Store

from django.shortcuts import render
from .controler import notification_controller as nc

from .controler import other_controller as oc
from .controler import api_controller as api_c
from .controler import email_controller as ec




class Pages:

    # Fetch Notification    

    def fetch_notifications(request): 
       print("Fetch Notification ...")
       return nc.fetch_message(request)



    # update Notification 

    def mark_notifications_as_read(request):
        print("Mark As Read Notification ....")
        return nc.read_message(request)
    
    # Home Page Render 

    def home(request):        
        # api_c.dhlApi(request=request)
        return render(request , 'interface_templates/home.html')
    

   # Store List 
    def store_list(request):
        stores = Store.objects.all()
        return render(request, 'interface_templates/store_list.html', {'stores': stores})
    
    # Help Page 
    def help(request):         
         return render(request ,"interface_templates/help.html" )
    
    

# Packages Detail Will Show 

    # @login_required(login_url='signin')  # Specify your login URL here
    # def package_details(request):
    #     return pc.package_details(request)



    # Generate  Barcodoe 

    def generate_barcode(profile):

     
        return oc.generate_barcode(profile)
    
    


# Uploading Package it is Admin View 





    def calculate_price_view(request):
    
            return render(request, 'interface_templates/calculate_price.html')




    def send_message(request):

        return ec.send_message(request)






    def dhlApi(request):     
        return api_c.dhlApi(request)

   # Mocked tracking data for demonstration
    def get_tracking_data(id):
       return api_c.get_tracking_data(id)
            

    def tracking_page(request):
        return render(request, 'interface_templates/tracking_page.html')
    

    def upload_shipment(request):
        return api_c.upload_shipment(request)


    def createLabel(request):

       api_c.createLabel(request)





    
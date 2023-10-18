from django.http import HttpResponse, JsonResponse
from interface.dhl.DHL_Info.packages_info import PackagesInfo
from interface.dhl.DHL_Info.reciever_info import Reciever
from interface.dhl.DHL_Info.sender_info import Sender
from interface.models import CustomUser
from interface.dhl.dhl_apis import calculate, dhlServices

def rates(request):
    print('Entered rates')
    dhl_service = dhlServices()
    print('dhl_service')
    package_length = request.POST.get('package_length')
    package_width = request.POST.get('package_width')
    package_height = request.POST.get('package_height')
    package_weight = request.POST.get('package_weight')
    
    user = request.user  

    try:
        customUser = CustomUser.objects.get(user=user)
    except CustomUser.DoesNotExist:
        print('no user')
      
        return HttpResponse("CustomUser for this user does not exist")
  
   
    sender_address = Sender.dhlSenderAddrerss(
        streetLine1='CA',
        postalCode='12121212',
        provinceCode='121212',
        countryCode='CA',
        cityName='New York'
    )
   

    
 
    reciever_address = Reciever.recieverAddress(
        streetLine1= customUser.address,
        postalCode=customUser.postal_code,
        countryCode=customUser.destinationCountry,
        cityName=customUser.city_name
    )

    package = PackagesInfo.packageToShip(
        packageHeight=package_height,
        packageLength=package_length,
        packageWeight=package_weight,
        packageWidth=package_width
    )
   
    dated = '12/7/2023'
    rate = calculate(package=package, senderAddress=sender_address, recieverAddress=reciever_address, date = dated)
    print("Rates:", rate)

    return JsonResponse({'rates': rate.success})



# def upload_shipment(request):
#     # if request.method == "POST":
#         # Replace with your DHL API credentials
#         api_key = settings.DHL_API_KEY
#         api_secret = settings.DHL_API_SECRET

#         # Replace with your actual DHL API endpoint for shipment creation
#         api_endpoint = "https://api-eu.dhl.com/shipment/create"

#         # Get form data from the frontend
#         tracking_number = '675564886'
#         # request.POST.get("trackingNumber")

#         weight =56
#         # request.POST.get("packageWeight")

#         destination_country ='AF'
#         # request.POST.get("destinationCountry")

#         # Construct headers
#         headers = {
#             'Accept': 'application/json',
#             'DHL-API-Key': api_key,
#             'DHL-API-Secret': api_secret,
#             'Content-Type': 'application/json'
#         }

#         # Construct payload
#         payload = {
#             "trackingNumber": tracking_number,
#             "weight": weight,
#             "destinationCountry": destination_country
#             # Add other required fields for shipment creation
#         }


#         # Make the API request
#         response = requests.post(api_endpoint, headers=headers, json=payload)
#         api_response = response.json()
#         print("Upload SuccessFully ",api_response)

#         return JsonResponse(api_response)

#     # return render(request, 'interface_templates/upload_shipment.html')




#   # Mocked tracking data for demonstration


# def get_tracking_data(id):
#         # Replace with your actual DHL API endpoint for tracking
#         api_endpoint = "https://api-eu.dhl.com/track/shipments"


#         # Replace with your DHL API credentials
#         api_key = settings.DHL_API_KEY
#         api_secret = settings.DHL_API_SECRET

#         # Replace with the actual tracking number

#         tracking_number = id

#         # Construct headers
#         headers = {
#             'Accept': 'application/json',
#             'DHL-API-Key': api_key,
#             'DHL-API-Secret': api_secret,
#         }

#         # Construct parameters
#         params = {
#             'trackingNumber': tracking_number,
#             'levelOfDetails': 'ALL_CHECK_POINTS',
#         }

#         # Make the API request
#         response = requests.get(api_endpoint, headers=headers, params=params)
#         print(response)
#         tracking_data = response.json()
#         print(tracking_data)

#         return tracking_data
        

    

# def dhlApi(request):

    

#     print("Enter Here ..")

#     AWB_NUMBER = '1234567890'  # Example AWB number for testing
#     API_KEY = 'Wjgw0r1yUNgJJnjcboDQ7P6xuDUOSSXW'  # Replace with your API key
#     API_SECRET = 'hXSfV9GFpWFOxT1D'  # Replace with your API secret

#     params = urlencode({
#         'trackingNumber': AWB_NUMBER,  # Provide the AWB number as 'trackingNumber'
#         'levelOfDetails': 'ALL_CHECK_POINTS'  # Specify the level of tracking details you need
#     })



#     headers = {
#         'Accept': 'application/json',
#         'DHL-API-Key': API_KEY,
#         'DHL-API-Secret': API_SECRET
#     }

#     connection = http.client.HTTPSConnection("api-eu.dhl.com")
#     print(connection, "Is Connection Stable...")

#     connection.request("GET", "/track/shipments?" + params, "", headers)
#     response = connection.getresponse()

#     status = response.status
#     reason = response.reason
#     data = json.loads(response.read())

#     print("Status: {} and reason: {}".format(status, reason))
#     print(data)

#     connection.close()
    
    
#     return render(request, 'interface_templates/home.html')








# def createLabel(request):

#         api_endpoint = "https://api.example.com/shipment-labels"

#         # Replace with your DHL API credentials
#         api_key = settings.DHL_API_KEY
#         api_secret = settings.DHL_API_SECRET

#         # Replace with the actual payload for creating the shipment label
#         payload = {
#             "shipment_details": {
#                 "sender": {
#                     "name": "Akhlaq",
#                     "address": "Pakistan"
#                     # ... other sender details
#                 },
#                 "receiver": {
#                     "name": "Jaleel",
#                     "address": "UAE"
#                     # ... other receiver details
#                 },
#                 # ... other shipment details
#             }
#         }

#         # Construct headers
#         headers = {
#             'Accept': 'application/json',
#             'DHL-API-Key': api_key,
#             'DHL-API-Secret': api_secret,
#         }

#         # Make the API request
#         response = requests.post(api_endpoint, headers=headers, json=payload)

#         # Process the response
#         if response.status_code == 200:
#             label_data = response.json()
#             # Process label_data as needed
#             print(label_data)
#         else:
#             print("Error creating shipment label:", response.status_code)
#             print(response.text)
  






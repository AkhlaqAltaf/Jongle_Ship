
import http
import json
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
import requests

from urllib.parse import urlencode



def upload_shipment(request):
    # if request.method == "POST":
        # Replace with your DHL API credentials
        api_key = settings.DHL_API_KEY
        api_secret = settings.DHL_API_SECRET

        # Replace with your actual DHL API endpoint for shipment creation
        api_endpoint = "https://api-eu.dhl.com/shipment/create"

        # Get form data from the frontend
        tracking_number = '675564886'
        # request.POST.get("trackingNumber")

        weight =56
        # request.POST.get("packageWeight")

        destination_country ='AF'
        # request.POST.get("destinationCountry")

        # Construct headers
        headers = {
            'Accept': 'application/json',
            'DHL-API-Key': api_key,
            'DHL-API-Secret': api_secret,
            'Content-Type': 'application/json'
        }

        # Construct payload
        payload = {
            "trackingNumber": tracking_number,
            "weight": weight,
            "destinationCountry": destination_country
            # Add other required fields for shipment creation
        }


        # Make the API request
        response = requests.post(api_endpoint, headers=headers, json=payload)
        api_response = response.json()
        print("Upload SuccessFully ",api_response)

        return JsonResponse(api_response)

    # return render(request, 'interface_templates/upload_shipment.html')




  # Mocked tracking data for demonstration


def get_tracking_data(id):
        # Replace with your actual DHL API endpoint for tracking
        api_endpoint = "https://api-eu.dhl.com/track/shipments"


        # Replace with your DHL API credentials
        api_key = settings.DHL_API_KEY
        api_secret = settings.DHL_API_SECRET

        # Replace with the actual tracking number

        tracking_number = id

        # Construct headers
        headers = {
            'Accept': 'application/json',
            'DHL-API-Key': api_key,
            'DHL-API-Secret': api_secret,
        }

        # Construct parameters
        params = {
            'trackingNumber': tracking_number,
            'levelOfDetails': 'ALL_CHECK_POINTS',
        }

        # Make the API request
        response = requests.get(api_endpoint, headers=headers, params=params)
        print(response)
        tracking_data = response.json()
        print(tracking_data)

        return tracking_data
        

    

def dhlApi(request):

    

    print("Enter Here ..")

    AWB_NUMBER = '1234567890'  # Example AWB number for testing
    API_KEY = 'Wjgw0r1yUNgJJnjcboDQ7P6xuDUOSSXW'  # Replace with your API key
    API_SECRET = 'hXSfV9GFpWFOxT1D'  # Replace with your API secret

    params = urlencode({
        'trackingNumber': AWB_NUMBER,  # Provide the AWB number as 'trackingNumber'
        'levelOfDetails': 'ALL_CHECK_POINTS'  # Specify the level of tracking details you need
    })



    headers = {
        'Accept': 'application/json',
        'DHL-API-Key': API_KEY,
        'DHL-API-Secret': API_SECRET
    }

    connection = http.client.HTTPSConnection("api-eu.dhl.com")
    print(connection, "Is Connection Stable...")

    connection.request("GET", "/track/shipments?" + params, "", headers)
    response = connection.getresponse()

    status = response.status
    reason = response.reason
    data = json.loads(response.read())

    print("Status: {} and reason: {}".format(status, reason))
    print(data)

    connection.close()
    
    
    return render(request, 'interface_templates/home.html')








def createLabel(request):

        api_endpoint = "https://api.example.com/shipment-labels"

        # Replace with your DHL API credentials
        api_key = settings.DHL_API_KEY
        api_secret = settings.DHL_API_SECRET

        # Replace with the actual payload for creating the shipment label
        payload = {
            "shipment_details": {
                "sender": {
                    "name": "Akhlaq",
                    "address": "Pakistan"
                    # ... other sender details
                },
                "receiver": {
                    "name": "Jaleel",
                    "address": "UAE"
                    # ... other receiver details
                },
                # ... other shipment details
            }
        }

        # Construct headers
        headers = {
            'Accept': 'application/json',
            'DHL-API-Key': api_key,
            'DHL-API-Secret': api_secret,
        }

        # Make the API request
        response = requests.post(api_endpoint, headers=headers, json=payload)

        # Process the response
        if response.status_code == 200:
            label_data = response.json()
            # Process label_data as needed
            print(label_data)
        else:
            print("Error creating shipment label:", response.status_code)
            print(response.text)
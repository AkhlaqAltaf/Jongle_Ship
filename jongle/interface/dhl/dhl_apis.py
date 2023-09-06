
# python dhl 

# from django.conf import settings
from python_dhl.service import DHLService
from python_dhl.resources import shipment , address

from zoneinfo import ZoneInfo
from python_dhl import service
from python_dhl.resources.helper import AccountType, IncotermCode, MeasurementUnit, ProductCode, ShipperType, TypeCode, next_business_day
import base64
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image
from io import BytesIO

import requests
# settings.configure()

class settings:

    DHL_API_KEY = 'Wjgw0r1yUNgJJnjcboDQ7P6xuDUOSSXW'
    DHL_API_SECRET = 'hXSfV9GFpWFOxT1D'
    DHL_ACCOUNT = '950250272'
    DHL_ACCOUNT_IMPORT = '950250272'
    DHL_ACCOUNT_EXPORT = '950250272'


with open('jongle/static/images/logo.png', 'rb') as logo_file:
    logo_base64 = base64.b64encode(logo_file.read()).decode('utf-8')



def dhlServices():


    service = DHLService(api_key=settings.DHL_API_KEY, api_secret=settings.DHL_API_SECRET,
                    account_number=settings.DHL_ACCOUNT_EXPORT,
                    test_mode=True)
    
    return service
    


def dhlAccount():

    accounts = [
shipment.DHLAccountType(type_code=AccountType.SHIPPER, number=settings.DHL_ACCOUNT_EXPORT),
]


    return accounts    


def dhlSenderContact():


    sender_contact = address.DHLContactInformation(
    company_name='Test Co.',
    full_name='Name and surname',
    phone='+39000000000',
    email='matteo.munaretto@innove.it',
    contact_type=ShipperType.BUSINESS.value
)
    
    return sender_contact
    
    


def  dhlSenderAddrerss():

    sender_address = address.DHLPostalAddress(
    street_line1='Via Maestro Zampieri, 14',
    postal_code='36016',
    province_code='VI',
    country_code='IT',
    city_name='Thiene',
)    
    
    return sender_address
    

def dhlSenderRegistration():

    registration_numbers = [address.DHLRegistrationNumber(
    type_code=TypeCode.VAT.name,
    number='42342423423',
    issuer_country_code='IT'
)]
    

    return registration_numbers





def recieverContact():


    receiver_contact = address.DHLContactInformation(
full_name='Customer',
phone='+39000000000',
email='matteo.munaretto@innove.it',
contact_type=ShipperType.PRIVATE.value
)
    
    return receiver_contact


def recieverAddress():


    receiver_address = address.DHLPostalAddress(
street_line1='Rue Poncelet, 17',
postal_code='75017',
country_code='FR',
city_name='Paris',
)
    

    return receiver_address



def packageToShip():

    packages = [shipment.DHLProduct(
weight=1,
length=35,
width=28,
height=8
)]
    

    return packages



def shipmentDate():


    shipment_date = next_business_day()
    shipment_date = shipment_date.replace(hour=14, minute=0, second=0, microsecond=0)
    shipment_date = shipment_date.replace(tzinfo=ZoneInfo('Europe/Rome'))



    return shipment_date


def addServices():

    added_service = [shipment.DHLAddedService(
service_code='W'
)]

    return added_service

def contentDhl():

    packages = packageToShip()


    content = shipment.DHLShipmentContent(
packages=packageToShip(),
is_custom_declarable=False,
description='Shipment test',
incoterm_code=IncotermCode.DAP.name,
unit_of_measurement=MeasurementUnit.METRIC.value,
product_code=ProductCode.EUROPE.value
)
    

    return content



def  dhlOutPut():

    output = shipment.DHLShipmentOutput(
dpi=300,
encoding_format='pdf',
logo_file_format='png',
logo_file_base64=logo_base64 
)

    

    print("Here is OutPut Showing",output)
    return output

def letsShipData():
    customer_references = ['id1', 'id2']

    
    s = shipment.DHLShipment(
    accounts=dhlAccount(),
    sender_contact=dhlSenderContact(),
    sender_address=dhlSenderAddrerss(),
    sender_registration_numbers=dhlSenderRegistration(),
    receiver_contact=recieverContact(),
    receiver_address=recieverAddress(),
    ship_datetime=shipmentDate(),
    added_services=addServices(),
    product_code=ProductCode.EUROPE.value,
    content=contentDhl(),
    output_format=dhlOutPut(),
    customer_references=customer_references,
)
    
    dhl_service = dhlServices()
    

    ship = dhl_service._create_shipment(dhl_shipment=s)

    

    rates = dhl_service.get_rates(dhlSenderAddrerss(), recieverAddress(), packageToShip(), shipmentDate())


    print(dir(ship))

# Check for specific attributes that indicate success or failure
    if hasattr(ship, 'success_indicator'):
        if ship.success_indicator:
            print("Shipment was successfully created!")
        else:
            print("Shipment creation failed.")
    else:
        print("Unable to determine shipment status.")

    # Print the entire response for debugging purposes
    print("Shipment Response:", ship)

    print("Rates....: ",rates)
    # self.assertTrue(ship.success)
    
    # print(ship)
    return s


if __name__=='__main__':

    letsShipData()


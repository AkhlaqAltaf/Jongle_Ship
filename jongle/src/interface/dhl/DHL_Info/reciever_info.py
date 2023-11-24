from python_dhl.resources import shipment , address
from python_dhl.resources.helper import AccountType, IncotermCode, MeasurementUnit, ProductCode, ShipperType, TypeCode
class Reciever:

    def recieverContact(fullName , phoneNo , email):


        receiver_contact = address.DHLContactInformation(
        full_name=      fullName ,       #'Customer',
        phone=          phoneNo   ,      #'+39000000000',
        email=          email      ,     #'matteo.munaretto@innove.it',
        contact_type=  ShipperType.PRIVATE.value
        )
        
        return receiver_contact


    def recieverAddress(streetLine1 , postalCode , countryCode , cityName):


        receiver_address = address.DHLPostalAddress(
        street_line1=    streetLine1,              #'Rue Poncelet, 17',
        postal_code=     postalCode,              #'75017',
        country_code=    countryCode,              #'FR',
        city_name=       cityName  ,               #'Paris',
        )
        


        return receiver_address
    
    




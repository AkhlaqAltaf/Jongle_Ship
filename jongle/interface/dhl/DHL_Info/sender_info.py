from python_dhl.resources import address, shipment
from python_dhl.resources.helper import AccountType, IncotermCode, MeasurementUnit, ProductCode, ShipperType, TypeCode
class Sender:


    def dhlSenderContact(companyName  , fullName ,  phoneNo  , emailAddress ):


        sender_contact = address.DHLContactInformation(
        company_name=  companyName ,                #'Test Co.',
        full_name=     fullName    ,                #'Name and surname',
        phone=         phoneNo     ,                #'+39000000000',
        email=         emailAddress,                #'matteo.munaretto@innove.it',
        contact_type=ShipperType.BUSINESS.value,
    )
        
        return sender_contact
    
    

    def  dhlSenderAddrerss(streetLine1 , postalCode , provinceCode , countryCode , cityName):

        sender_address = address.DHLPostalAddress(
        street_line1=   streetLine1 ,          #'Via Maestro Zampieri, 14',
        postal_code=    postalCode   ,          #'36016',
        province_code=   provinceCode ,         #'VI',
        country_code=    countryCode   ,         #'IT',
        city_name=       cityName      ,         #'Thiene',
        )    

        return sender_address
        

    def dhlSenderRegistration(reNumber , countryCode):

        registration_numbers = [address.DHLRegistrationNumber(
        type_code=TypeCode.VAT.name,
        number=              reNumber  ,             #'42342423423',
        issuer_country_code= countryCode ,           #'IT'
        )]
        

        return registration_numbers


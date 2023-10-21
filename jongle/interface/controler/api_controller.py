from django.http import HttpResponse, JsonResponse
import datetime
import logging
from interface.dhl.DHL_Info.packages_info import PackagesInfo
from interface.dhl.DHL_Info.reciever_info import Reciever
from interface.dhl.DHL_Info.sender_info import Sender
from interface.models import CustomUser
from interface.dhl.dhl_apis import calculate

def rates(request):
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s [%(levelname)s]: %(message)s',
        handlers=[
            logging.FileHandler('app.log'),
            logging.StreamHandler()
        ]
    )

    logging.debug('Entered rates')

    package_length = (request.POST.get('package_length', 0))
    package_width = (request.POST.get('package_width', 0))
    package_height = (request.POST.get('package_height', 0))
    package_weight = (request.POST.get('package_weight', 0))

    with_customs = request.POST.get('with_customs', 'false')  # Default to 'false'
    unit_of_measurement = request.POST.get('unit_of_measurement', 'kg')  # Default to 'kg'

    user = request.user

    try:
        customUser = CustomUser.objects.get(user=user)
    except CustomUser.DoesNotExist:
        logging.error('CustomUser not found for user: %s', user)
        return HttpResponse("CustomUser for this user does not exist")

    
    
    sender = Sender.dhlSenderAddress(
        streetLine1="Via Maestro Zampieri, 14",
        postalCode="36016",
        provinceCode="VI",
        countryCode="IT",
        cityName="Thiene"
    )
    
    receiver = Reciever.recieverAddress(
        streetLine1=customUser.address,
        postalCode=customUser.postal_code,
        countryCode=customUser.destinationCountry,
        cityName=customUser.city_name
    )

    product = PackagesInfo.packageToShip(
        height=package_height,
        length=package_length,
        weight=package_weight,
        width=package_width
    )
    
    

    logging.debug('Received package data: %s', product)

    # Construct the shipment date
    date = datetime.datetime(2023, 10, 21, 12, 0, 0, tzinfo=datetime.timezone.utc)

    rate = calculate(
        sender=sender,
        receiver=receiver,
        product=product,
        shipment_date=date,
        with_customs=with_customs,
        unit_of_measurement=unit_of_measurement
    )

    if not rate.success:
        logging.error('Failed to get rates: %s', rate)

        if hasattr(rate, 'error_message'):
            logging.error('Error message: %s', rate.error_message)
        else:
            logging.error("Unknown error occurred. No error message available.")
            logging.debug("Full rate response: %s", rate)  # Log the full response for debugging

    return JsonResponse({'rates': rate.success})
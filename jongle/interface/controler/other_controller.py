import barcode
from io import BytesIO


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
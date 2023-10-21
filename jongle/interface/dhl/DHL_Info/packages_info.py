# from python_dhl.resources import shipment

# class PackagesInfo:
#     @staticmethod
#     def packageToShip(packageWeight, packageLength, packageWidth, packageHeight):
#         dhl_product = shipment.DHLProduct(
#             weight=packageWeight,
#             length=packageLength,
#             width=packageWidth,
#             height=packageHeight
#         )
        
#         # Create a dictionary from the DHLProduct object
#         package = {
#             'packageWeight': dhl_product.weight,
#             'packageLength': dhl_product.length,
#             'packageWidth': dhl_product.width,
#             'packageHeight': dhl_product.height
#         }
#         return package

from python_dhl.resources import shipment

class PackagesInfo:
    @staticmethod
    def packageToShip(weight, length, width, height):
        dhl_product = shipment.DHLProduct(
            weight=weight,
            length=length,
            width=width,
            height=height
        )
        return dhl_product


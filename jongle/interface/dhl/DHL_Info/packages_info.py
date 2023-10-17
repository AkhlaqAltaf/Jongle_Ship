from python_dhl.resources import address, shipment
class PackagesInfo:

    def packageToShip(packageWeight , packageLength , packageWidth , packageHeight):

        packages = [shipment.DHLProduct(
        weight=packageWeight,
        length=packageLength,
        width=packageWidth,
        height=packageHeight
        )]

        return packages



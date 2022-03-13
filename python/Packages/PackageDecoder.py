from python.Packages.Packages import B_PackageDecoder


class PackageDecoder(B_PackageDecoder):

    def __init__(self, data: bytearray):
        B_PackageDecoder.__init__(self, data)

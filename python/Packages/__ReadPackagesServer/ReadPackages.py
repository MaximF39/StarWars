from .ReadPackagesClient import ReadPackagesClient
from ..PackageDecoder import PackageDecoder

class ReadPackages:
    decoder = PackageDecoder()
    read_packes = ReadPackagesClient()
    num_pack = 0

    def __init__(self, pack):
        self.decoder.data = pack
        while True:
            self.num_pack += 1
            PackNumber = self.decoder.read_int()
            res = self.read_packes.processPackages(PackNumber, self.decoder)
            if self.num_pack > 30:
                print(f'{PackNumber}, {res}')

            if len(self.decoder.data) == self.decoder.Position:
                break




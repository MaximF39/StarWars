

pack = bytearray(b'\xf3k\xca\x88\xf0\x01\x00\x00\x11\x00\x00\x00\x9a\x99\x99>ff\xa6?\x00\x00\x00\x00\x0e\x00\x00\x00\x01\x00\x00\x00?\x04\x19\xbb?\xa5L\xcd\x9c\x1fA*\xa0\x91\xa0\xe6\xe8\x03\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x01X\x00\x00\x00*\x1e\xda\xf4\xddVF"\xb6\x083n\x11\xa1m>\xe8\x03\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x01L\x00\x00\x00r\x8e\xd8\x9c\xb9\xf2A]\x82\xeaOF\x89\x9boL\xe8\x03\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x01\\\x00\x00\x00\xfd\x95\xe4\xcb\x91\xbdB\x0c\x9c\xb1\x14\xc8\x8d\xae\xd0\x8b\xe8\x03\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x01{\x00\x00\x00\xc7b\x14lV-Jz\x98\xb3\x8fs\x18X\xf0\xfd\xe8\x03\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x01\xba\x00\x00\x003\xe5\x14v\xd1jC\xa7\xbe[\xe9\x9e{\t\xcb\xf8\xe8\x03\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x01j\x00\x00\x00\x15jz\xa7\xaf\x04I\x12\xa2\xf2\xf9EI&=\'\xe8\x03\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x01\xbf\x00\x00\x00\xce&\xea1\xfd\x92E\x15\x84\x00\xc0\xdc\xe3\xd4\x07\xae\xe8\x03\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x01<\x00\x00\x00\xd3\x98\xab\x18;\xa1Le\x82\xe9$\x8d\xdd~\xc3\xa2\xe8\x03\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x01P\x00\x00\x00?\xba\xc5\xb3\xeaVO\xb8\xb4ga\xc9\xf3\xc8\x02\xca\xe8\x03\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x01E\x00\x00\x00\xa4\xbe\xc5?\xfa\x05Li\xb6\x8eg\x99\xdc\xc1TD\x01\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x01b\x00\x00\x00\xda\xd4\xb7\xfc\x15\xf5@\x8e\xb5\xf7J\x81\x97\xde\xc9"\x01\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x01c\x00\x00\x00\xa9\x18"0O\x1fB\x1b\xb75\xfe~Y3\x00\x99\x01\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x01v\x00\x00\x00\x11\x95\xb4\xe3\xcd\xa1E\xe3\xb1\xcc\xb3\x16\x00+r=\x01\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x01')


from ReadPackagesClient import ReadPackagesClient
from PackageDecoder import PackageDecoder

decoder = PackageDecoder()
decoder.data = pack
print(decoder.read_int())
print(decoder.read_int())
# print(decoder.read_int())
# print(decoder.read_float())
# print(decoder.read_float())
print(ReadPackagesClient().tradingItems(decoder))

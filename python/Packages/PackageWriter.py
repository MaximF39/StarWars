import math
import struct
from datetime import datetime


class PackageWriter:
    PackageNumber: int
    data: bytearray = bytearray()

    def get_package(self) -> bytearray:
        loc1 = 1619022605998 + datetime.now().time().hour + datetime.now().time().minute
        loc1 /= 1000
        while loc1 > 2147483648:
            loc1 -= 2147483648
        loc1 = math.floor(loc1)
        loc2 = math.floor(loc1 / 1721)
        loc3 = 0
        for i in self.data:
            loc3 += i
            if loc3 > 3719:
                loc3 -= 3719
        pack = self.converter(self.PackageNumber, "i")
        # pack = self.byte_writer(pack, self.converter(loc1, "i"))
        # pack = self.byte_writer(pack, self.converter(loc2 - loc3, "i"))
        pack = self.byte_writer(pack, self.converter(len(self.data), "i")) #Сомнительно
        return self.byte_writer(pack, self.data)

    @staticmethod
    def converter(value: float, bytes_type: str) -> bytearray:
        return bytearray(struct.pack(bytes_type, value))

    def write_utf(self, string: str) -> None:
        str_bytes = bytes(string, 'utf-8')
        self.write_short(len(str_bytes))
        self.write_bytes(str_bytes)

    def write_double(self, double: float) -> None:
        self.data.append(*self.byte_writer(self.data, self.converter(double, "d")))

    def write_int(self, int_: int) -> None:
        self.data.append(*self.byte_writer(self.data, self.converter(int_, "i")))

    def write_float(self, float_: float) -> None:
        self.data.append(*self.byte_writer(self.data, self.converter(float_, "f")))

    def write_short(self, short: float) -> None:
        self.data.append(*self.byte_writer(self.data, self.converter(short, "h")))

    def write_unsigned_byte(self, byte: bytes) -> None:
        self.data.append(*self.byte_writer(self.data, bytearray(byte)))

    def write_bool(self, bool_: bool) -> None:
        self.data.append(*self.byte_writer(self.data, self.converter(bool_, "?")))

    def write_bytes(self, bytearray_: [bytearray, bytes]) -> None:
        self.data.append(*self.byte_writer(self.data, bytearray_))

    @staticmethod
    def byte_writer(one_byte_array: [bytearray, bytes], two_byte_array: [bytearray, bytes]) -> bytearray:
        res = bytearray(one_byte_array)
        for i in two_byte_array:
            res.append(i)
        return res

    def getPackage(self):
        pass

    def writeSkill(self):
        pass

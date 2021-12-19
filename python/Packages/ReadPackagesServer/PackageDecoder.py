import struct


class PackageDecoder:
    data = bytearray()

    Position = 0

    def decoder(self, type, buffer):
        return struct.unpack(type, buffer)[0]

    def read_utf(self) -> str:
        stringLen = self.read_unsigned_byte()
        self.Position += 1
        return self.read_bytes(stringLen).decode("utf-8")

    def read_double(self) -> float:
        return self.decoder("d", self.read_bytes(8))

    def read_int(self) -> int:
        return self.decoder("i", self.read_bytes(4))

    def read_float(self) -> float:
        return self.decoder("f", self.read_bytes(4))

    def read_short(self) -> int:
        return self.decoder("h", self.read_bytes(2))

    def read_bool(self) -> bool:
        return self.decoder("?", self.read_bytes(1))

    def read_unsigned_byte(self):
        return self.read_bytes(1)[0]

    def read_bytes(self, ByteLength) -> bytearray:
        if ByteLength > (len(self.data) - self.Position):
            return bytearray(0)
        buffer = bytearray(ByteLength)
        if self.Position + len(buffer) <= len(self.data):
            for i in range(len(buffer)):
                buffer[i] = self.data[self.Position + i]
        self.Position += len(buffer)
        return buffer



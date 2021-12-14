import struct


class PackageDecoder:
    data: bytearray = bytearray()
    position: int

    @staticmethod
    def decoder(type_: str, buf: bytes) -> tuple:
        return struct.unpack(type_, buf)[0]

    def read_utf(self) -> str:
        string_len = self.read_unsigned_byte()
        self.position += 1
        return self.read_bytes(string_len).decode("utf-8")

    def read_double(self) -> tuple:
        return self.decoder("d", self.read_bytes(8))

    def read_int(self) -> tuple:
        return self.decoder("i", self.read_bytes(4))

    def read_float(self) -> tuple:
        return self.decoder("f", self.read_bytes(4))

    def read_short(self) -> tuple:
        return self.decoder("h", self.read_bytes(2))

    def read_boolean(self) -> tuple:
        return self.decoder("?", self.read_bytes(1))

    def read_unsigned_byte(self) -> int:
        return self.read_bytes(1)[0]

    def read_bytes(self, byte_length: int) -> bytearray:
        buffer = bytearray(byte_length)
        if self.position + len(buffer) <= len(self.data):
            for i in range(len(buffer)):
                buffer[i] = self.data[self.position + i]
        self.position += len(buffer)
        return buffer

    def is_correct_read(self) -> bool:
        if self.position == len(self.data):
            return True
        return False

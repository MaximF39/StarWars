

s = [bytearray(b'\xcdk\xca\x88\t\x00\x00\x00\x07\x000.9.0.1'), bytearray(b'\xcdk\xca\x88\t\x00\x00\x00\x07\x000.9.0.1')]

print(s)

e = bytearray()
for i in range(len(s)):
    e.append(s[i])

print(e)
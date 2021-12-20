guid = bytearray()
num_guid = 0
for i in range(16):
    guid.append(0)

pos = 0
while num_guid:
    guid[pos] = num_guid % 256
    num_guid //= 256
    pos += 1

print(len(guid))
print(bin(128))
print(bin(3))
print(bin(5))
print(bin(1024))

result = [int(v) for v in format(128, "b")][::-1]
print(result)

text = "Hello, world."
result = [format(ord(c), "b") for c in text]
print(result)

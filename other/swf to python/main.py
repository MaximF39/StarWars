del_element = ['{', '}', 'private', 'public', 'var', ';', 'static', 'new', 'override', 'const', 'protected', 'def _set', 'def get_packages',
               '.instance']
replace_element = [[': void', '-> None:'], [': Boolean', "-> bool:"], ['Boolean', "bool"], ['true', "True"], ['false', "False"],
                   [": Number", '-> float:'], ["Number", 'float'], ['function', 'def'], [": ByteArray", '-> bytearray:'],
                   ["ByteArray", 'bytearray'], ['push', 'append'], ['||', 'or'], ['null', 'None'],
                   ['++', '+= 1'], ['Array', 'list'], ["catch", 'except:'], ['try', 'try:'],
                   ['&&', 'and'], ['!', 'not '], ['not =', '!='], ["undefined", 'None'],
                   ['else', 'else:'], ['NaN', 'None'], [": String", '-> str'], ['String', 'str'], ['switch', 'match'],
                   ['this', 'self'], ['Math', 'math'], ['uint', 'int']]

dop = [['readUTF', 'write_utf'], ['readInt', 'write_int'], ['readShort', 'write_short'],
       ['readUnsignedByte', 'write_unsigned_byte'], ["readBytes", 'write_bytes'],
       ['readBoolean', 'write_bool'], ['Converter', 'converter'], ["readDouble", 'write_double'],
       ['readFloat', 'write_float'], ['readbool', 'write_bool'], ['readGuid', 'write_guid'], ['readByte', 'write_bytes'],
       ['readItems', 'write_items'], ['readSkills', 'write_skills']]
dop2 = [['read_utf', 'write_utf'], ['read_int', 'write_int'], ['read_short', 'write_short'],
       ['read_unsigned_byte', 'write_unsigned_byte'], ["read_bytes", 'write_bytes'],
       ['read_boolean', 'write_bool'], ['Converter', 'converter'], ["readDouble", 'write_double'],
       ['read_float', 'write_float'], ['read_bool', 'write_bool'], ['read_guid', 'write_guid'], ['read_bytes', 'write_bytes'],
       ['read_items', 'write_items'], ['read_skills', 'write_skills']]

# for i in dop:
#     replace_element.append(i)

with open('file.txt', 'r', encoding='UTF-8') as f:
    data = f.read()


for e in replace_element:
    data = data.replace(e[0], e[1])

for e in del_element:
    data = data.replace(e, '')

with open('test.py', 'w') as f:
    f.write(data)
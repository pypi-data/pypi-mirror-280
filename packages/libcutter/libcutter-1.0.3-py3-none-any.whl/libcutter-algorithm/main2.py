from decrypt_file import *

data1 = 'Hello, world'


def str_to_bytes(msg):
    return ' '.join(format(ord(x), 'b') for x in msg)

n = 6
l = len(str_to_bytes(data1))
key = 18365801009696695577
print(l)
data = decrypt_data_from_image('file.bin', key, 3, l, n)

print(data)


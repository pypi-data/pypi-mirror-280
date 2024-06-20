from encrypt_file import *

n = 6

data = 'Hello, world'

data = str_to_bytes(data)

key = encrypt_data_in_image(data, 'image.jpeg', 'file.bin', 1, n)
save_encrypted_image('enc.jpeg')

print(key)

import random


def create_binary_files():
    for i in range(10):
        file_name = f'{i+1}.bin'
        with open(file_name, 'wb') as f:
            data = bytearray([random.randint(0, 255) for _ in range(1024 * 1024)])
            f.write(data)


create_binary_files()

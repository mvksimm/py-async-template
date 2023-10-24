import datetime
import time

from get_files import get_file_names


def read_file(filename):
    with open(filename, mode='rb') as f:
        print(filename)
        while True:
            time.sleep(0.001)
            data = f.read(1024)
            if not data:
                print(filename, "done ###############")
                break


def main():
    begin = datetime.datetime.now()
    files = get_file_names()
    for f in files:
        read_file(f)
    print(datetime.datetime.now() - begin)


main()

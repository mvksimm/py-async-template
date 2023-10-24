import argparse
import os


def get_file_names():
    parser = argparse.ArgumentParser()
    parser.add_argument('directory')
    args = parser.parse_args()
    if not os.path.isdir(args.directory):
        raise ValueError("Путь не является директорией")
    return [os.path.join(args.directory, name) for name in os.listdir(args.directory)]

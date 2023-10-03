import os


def get_file_names(argv):
    if len(argv) == 1:
        raise ValueError("Путь не передан")
    if not os.path.isdir(argv[1]):
        raise ValueError("Путь не является директорией")
    return [os.path.join(argv[1], name) for name in os.listdir(argv[1])]

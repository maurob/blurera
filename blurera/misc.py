import os


def trim_ext(filename):
    name, ext = os.path.splitext(filename)
    return name

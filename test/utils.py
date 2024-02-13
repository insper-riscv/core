import os


def source(name):
    dir = os.path.dirname(os.path.dirname(__file__))
    dir = os.path.join(dir, "src")
    return os.path.join(dir, name)

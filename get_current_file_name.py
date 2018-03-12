"""
Get the current file name.
"""


import os


def main():
    name, ext = os.path.splitext(__file__)
    return name, ext


if __name__ == '__main__':
    name, ext = main()
    print(name)

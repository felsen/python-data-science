"""
simple decorator basics.
"""

from functools import wraps
import logging


def debug(func):

    msg = func.__qualname__  # applicable only in Python3.x version

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Calling {}".format(msg))
        f = func(*args, **kwargs)
        print(f)
        return "Ending {}".format(msg)

    return wrapper


def debug_1(func):

    msg = func.__qualname__  # applicable only for python 3.x version
    log = logging.getLogger(func.__module__)

    @wraps(func)
    def wrapper(*args, **kwargs):
        log.info(msg)
        return func(*args, **kwargs)
    return wrapper


@debug
@debug_1
def add(x, y):
    c = x + y
    return c

print(add(10, 5))


@debug
@debug_1
def sub(x, y):
    c = x - y
    return c

print(sub(10, 5))


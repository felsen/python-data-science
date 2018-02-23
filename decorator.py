"""
simple decorator basics.
"""

from functools import wraps, partial
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


def debug_arg(prefix=""):

    def decorate(func):

        msg = "{} {}".format(prefix, func.__qualname__)

        @wraps(func)
        def wrapper(*args, **kwargs):
            print(msg)
            return func(*args, **kwargs)

        return wrapper

    return decorate


def debug_arg_1(func=None, *, prefix=""):

    if func is None:
        return partial(debug_arg_1, prefix=prefix)

    msg = "{} {}".format(prefix, func.__qualname__)

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(msg)
        return func(*args, **kwargs)

    return wrapper


@debug_arg_1(prefix="*****")
@debug
@debug_1
def add(x, y):
    c = x + y
    return c


print(add(10, 5))


@debug_arg_1(prefix="*****++++")
@debug
@debug_1
def sub(x, y):
    c = x - y
    return c


print(sub(10, 5))

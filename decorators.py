"""
Decorator Implementation.

There, are three way of implementating decorator, Based on Django,.....

1) Basic Decorator
   Example: first_decorator() function

2) Parameterized Decorator(passing argument to the decorator function itself)
   Example: second_decorator() function

3) Class Decorator
   Example: third_decorator() function

Ref:

http://scottlobdell.me/2015/04/decorators-arguments-python/
https://mrcoles.com/blog/3-decorator-examples-and-awesome-python/
https://www.saltycrane.com/blog/2010/03/simple-python-decorator-examples/

"""


from functools import wraps
from django.http import HttpResponse


def first_decorator(view_func):

    def _decorator(view_func, *args, **kwargs):
        # Before calling function
        res = view_func(*args, **kwargs)
        # After calling function
        return res
    return wraps(view_func)(_decorator)


def first_decorator(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        # Before calling function
        res = f(*args, **kwargs)
        # After calling function
        return res
    return wrapped


"""

@first_decorator
def any_func_name(request):
    return HttpResponse("Yes")

"""


def second_decorator(extra_value=None):
    
    def _my_decorator(view_func):

        def _decorator(request, *args, **kwargs):
            # Before calling function
            f = view_func(*args, **kwargs)
            # After calling function
            return f

        return wraps(view_func)(_decorator)

    return _my_decorator


def second_decorator(extra_value=None):

    def true_decorator(f):

        @wraps(f)
        def wrapped(*args, **kwargs):
            # Before calling function
            res = f(*args, **kwargs)
            # After calling function
            return res

        return wrapped

    return true_decorator


"""

@second_decorator(extra_value=3)
def any_func_name(request):
    return HttpResponse("Yes")

"""


class My_Decorator(object):

    def __init__(self, view_func):
        self.view_func = view_func
        wraps(view_func)(self)

    def __call__(self, request, *args, **kwargs):
        # Before calling function
        res = self.view_func(*args, **kwargs)
        # After calling function
        return res


"""
@My_Decorator
def any_func_name(request):
    return HttpResponse("Yes")
"""

"""_summary_
A decorator is a function that accepts a function as input and returns a new function as
output.
"""


import logging
import time
from functools import wraps
#https://stackoverflow.com/questions/308999/what-does-functools-wraps-do

# this decorator is implemented as a class that is whhy
#   we need to use __call__ method

class CacheDecorator:
    def __init__(self, original_func) -> None:
        self.org_func = original_func
        self._cache_dict = dict()
        
    def __call__(self, *args, **kwargs):
        
        if args in self._cache_dict:
            return self._cache_dict[args]
        
        result = self.org_func(*args)
        self._cache_dict[args] = result
        return result


class LoggingDecorator:
    def __init__(self, original_func) -> None:
        self.org_func = original_func
        wraps(original_func)(self) # this is used when using decorator chaining to preserve which function is called
    
    
    def __call__(self, *args, **kwargs):
        logging.basicConfig(level=logging.INFO)
        logging.info("Input to %s = %s", self.org_func.__name__, args)
        return self.org_func(*args)
    
    
def fibonacci_with_cache(n, cache=None):
    if n in cache:
        return cache[n]
    
    if n <= 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonacci_with_cache(n - 1) + fibonacci_with_cache(n - 2)
    
    cache[n] = result
    return result

   
# @LoggingDecorator
@CacheDecorator
def fib(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2) # everytime this fib func is called a decorator will be called

start = time.time()
res = fib(10)
print("Total time =", time.time() - start)
print(res)


# n = 10
# print(f"Fibonacci({n}) =", fibonacci_with_cache(n, []))
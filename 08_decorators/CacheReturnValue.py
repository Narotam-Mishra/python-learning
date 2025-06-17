
#
# Implement a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function.
# 

import time

def cache(func):
    cache_value = {}
    print("Cache Values:", cache_value)
    def wrapper(*args):
        # print("Cache Values:", cache_value)
        if args in cache_value:
            return cache_value[args]
        res = func(*args)
        cache_value[args] = res
        return res
    return wrapper

@cache
def long_running_function(a, b):
    time.sleep(4)
    return a + b

print("first call:",long_running_function(2, 3))
print("second call:",long_running_function(2, 3))
print("third call:",long_running_function(5, 9))
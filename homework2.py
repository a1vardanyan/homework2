#profiler
import time

def profiler(func):
    def wrapper(value):
        wrapper.__doc__ = func.__doc__
        wrapper.last_time_taken = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        wrapper.calls += 1
        return func(value)
    wrapper.calls = 0
    return wrapper

@profiler
def sleepy_recursion(num_calls):
    """I am a strange sleepy recursive function"""
    print("hey")
    if num_calls > 1:
        sleepy_recursion(num_calls - 1)



print(sleepy_recursion(4))
print(sleepy_recursion.__doc__)
print(sleepy_recursion.last_time_taken)
print(sleepy_recursion.calls)

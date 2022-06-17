# decorators super charge or add extra features to an function

# in python function is first class citizen
# means functions can be used as variables

def hello(func):
    return func()

def greet():
    return "hi there! This is test"

my_var = greet
del greet

print(hello(my_var)) 
# print(greet())

# HOC : Higher Order Function
# function which eccept or returns another function

# decoratiors example
def my_decorator(func):
    def wrap_func(*args, **kwargs):    # wrap function wrapped the passed function
        print("*" * 10)
        func(*args, **kwargs)
        print("*" * 10)
    return wrap_func

@my_decorator
def cill_bill():
    print("Chull Bull Pandey 😁")

# cill_bill()

@my_decorator
def with_arguments(greeting, emoji = ':)'):
    print(greeting, emoji)

# with_arguments('bla bla bla', '😊😊')


# ########################
# why do we need decorator huh ??

from time import time

def perofrmance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f"took {t2 - t1} ms")
        
        if result < 5:
            print("Mara kha")
        else:    
            return result
    return wrapper

@perofrmance
def long_time():
    sum = 0
    for i in range(3):
        sum = i ** 2
    return sum

print(long_time())
# special type of thing in python that allow us
# to use special keyword yield, which can pause and
# resume function. Example: range() is a generator.
# Generator function must have range function and
# yield keyword

def generator_function(num):
    for i in range(num):
        yield i


g = generator_function(100)
# next(g)
# next(g)
# print(next(g))


# under the hood of generators and iterators

# this is how for loop work
def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break

# special_for([1,2,3])

# create range function


class MyGen():
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


# gen = MyGen(0, 10)
# for i in gen:
#     print(i)


# fibonacci numbers
# using generators
def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a     # yield is kind of return, but it returns a single product at a time then forget about that.
        temp = a
        a = b
        b = temp + b


# using list
def fib(number):
    a = 0
    b = 1
    result = []
    for i in range(number):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result


for x in fib(20):
    print(x)
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


gen = MyGen(0, 100)
for i in gen:
    print(i)
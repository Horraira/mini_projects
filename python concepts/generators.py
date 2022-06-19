# special type of thing in python that allow us to use special keyword yield, which can pause and resume function. Example: range() is a generator. Generator function must have range function and yield keyword

def generator_function(num):
    for i in range(num):
        yield i


g = generator_function(100)
next(g)
next(g)
print(next(g))


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

special_for([1,2,3])

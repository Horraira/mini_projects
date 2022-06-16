from array import array
from functools import reduce

def multiply2(item):
    return item * 2

def only_odd(item):
    return item % 2 != 0

def accumulator(acc, item):
    return acc + item

my_list = [14,11,15]
your_list = [140,101,150]
their_list = [84,19,35]

# map
# do some operation for each item of iterables
print(list(map(multiply2, my_list)))

# filter
# work with true or false value
print(list(filter(only_odd, my_list)))

# zip
# zip many iterables together
print(list(zip(my_list, your_list, their_list)))

# reduce
print(reduce(accumulator, my_list, 0))

print('#' * 20)
# lambda expresions
print(my_list)
print(reduce(lambda acc, item: acc + item, my_list, 0))
print(list(map(lambda item : item * item, my_list)))
# print(reduce(lambda acc, item: acc.append(item) if item[1] < acc.pop()[1] else 2, ['']))

my_li = [14,11,15,(11,12)]
print(my_li.pop()[1])
my_li.append(20)
print(my_li)

# sorting a list by second item of tuple
arr = [(0,2), (4,3), (10,-1), (9,9)]
arr.sort(key=lambda item: item[1])
print(arr)
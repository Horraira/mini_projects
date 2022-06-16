# list comprehension

from multiprocessing.sharedctypes import Value


my_list = [letter for letter in 'NAHAR']
# print(my_list)

my_list2 = [num for num in range(20)]
# print(my_list2)

my_list3 = [num * 2 for num in range(20)]
# print(my_list3)

my_list4 = [num * 2 for num in range(20) if num % 2 == 0]
print(my_list4)

# set comprehension

my_set = {letter for letter in 'NAHAR'}
# print(my_list)

my_set2 = { num for num in range(20) }
# print(my_list2)

my_set3 = { num * 2 for num in range(20) }
# print(my_list3)

my_set4 = { num * 2 for num in range(20) if num % 2 == 0 }
print(my_set4)

# dict comprehension

simpple_dict = {
    'a': 2,
    'b': 3
}

my_dict = {key : value ** 3 for key,value in simpple_dict.items()}
print(my_dict)

my_dict2 = {key : value ** 3 for key,value in simpple_dict.items() if value % 2 == 0}
print(my_dict2)
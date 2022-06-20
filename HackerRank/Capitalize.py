# def capitalize(name):
#     break_string = " ".join([atom.capitalize() for atom in name.split() if atom[0].isalpha() or atom])
#
#     print(break_string)


def solve(s):
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    print(s)


# b = "Hello, World!"
# print(b[:5])     # slicing, return the obj
# print(b.split())    # split, return an array
# print(b[:].split())
# print("45asd".capitalize())

name2 = input("Enter Your name: ")
solve(name2)

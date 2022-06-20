N = int(input())
l = len(bin(N)) - 2
print(str(l))
for i in range(1, N + 1):
    text = ""
    for c in "doXb":
        if text:
            text += " "
        text += "{:>" + str(l) + c + "}"
    print(text.format(i, i, i, i))

# print("{:>10b}".format(10))
# :> left align with space of l
# see string format for more
# d = decimal,o = Octal, X = hex, b = binary
# print("{:>4d} {:>4o} {:>4x} {:>4b}".format(10, 10, 10, 10))
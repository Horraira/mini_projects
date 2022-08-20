message = str(input("Enter message: ")).replace(" ", '1')


def preChar(alpha):
    return chr(ord(alpha) - 1)


def nextChar(alpha):
    return chr(ord(alpha) + 1)


enMessage = ' '.join(list(map(preChar, message)))
deMessage = ' '.join(list(map(nextChar, message)))


print('SENHAS Message:', enMessage.replace(" ", "").replace("0", " "))
print('Normal Message:', deMessage.replace(" ", "").replace("2", " "))
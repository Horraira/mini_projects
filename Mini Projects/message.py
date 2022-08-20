def preChar(alpha):
    return chr(ord(alpha) - 1)


def nextChar(alpha):
    return chr(ord(alpha) + 1)


print("**********   SENT MESSAGE   **********")
enMessage = ' '.join(list(map(preChar, str(input("Normal message: ")).replace(" ", '1'))))
print('SENHAS Message:', enMessage.replace(" ", "").replace("0", " "))


print("**********   RECEIVED MESSAGE   **********")
deMessage = ' '.join(list(map(nextChar, str(input("SENHAS message: ")).replace(" ", '1'))))
print('Normal Message:', deMessage.replace(" ", "").replace("2", " "))
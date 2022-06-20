s = input("Enter a string: ")

stuart = 0
kelvin = 0
vowel = 'AEIOU'
for i in range(len(s)):
    if s[i] in vowel:
        kelvin += (len(s)-i)
    else:
        stuart += (len(s)-i)

if kelvin > stuart:
    print("Kevin", kelvin)
elif kelvin < stuart:
    print("Stuart", stuart)
else:
    print("Draw")

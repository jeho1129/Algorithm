str = input()
result = ''
for i in range(len(str)):
    if str[i].islower():
        result += str[i].upper()
    else:
        result += str[i].lower()
print(result)
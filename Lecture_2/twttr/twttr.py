string = input("Input: ")
string_casefold = string.casefold()
for i in range(len(string_casefold)):
    if string_casefold[i] not in ['a', 'e', 'i', 'o', 'u']:
        print(string[i], end="")
print()

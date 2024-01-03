string = input("Input: ")
string_casefold = string.casefold()
for i in string_casefold:
    if i != "a" | i != "e" | i != "i" | i != "o" | i != "u":
        print()

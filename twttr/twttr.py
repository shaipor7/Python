string = input("Input: ")
string_casefold = string.casefold()
for i in range(len(string_casefold)):
    if string_casefold[i] != "a":
    # | i != "e" | i != "i" | i != "o" | i != "u":
        print(string[i], end="")
print()

string = input("Input: ")
for i in string:
    if i.islower():
        print(i, end="")
    else: print("_"+i.casefold(), end="")
print()

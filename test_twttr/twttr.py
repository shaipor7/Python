def main():
    string = input("Input: ")
    a = shorten(string)
    print(a)

def shorten(string):
    A=""
    string_casefold = string.casefold()
    for i in range(len(string_casefold)):
        if string_casefold[i] not in ['A', 'E', 'I', 'O', 'U'] and not string_casefold[i].isnumeric() \
        and string_casefold[i] != ".":
            A+=string[i]
    return A

if __name__ == "__main__":
    main()

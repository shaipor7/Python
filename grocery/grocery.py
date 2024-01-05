dict = {}

while True:
    try:
        string = input("")
        dict[string] = dict.get(string, 0) + 1
    except EOFError:
        for item in sorted(dict.keys()):
            print(f"{dict[item]} {item.upper()}")


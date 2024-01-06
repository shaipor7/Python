string = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
string = string.casefold().strip().replace(" ","-")
match string:
    case "42" | "forty-two":
        print("Yes")
    case _:
        print("No")

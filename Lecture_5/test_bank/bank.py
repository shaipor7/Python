def main():
    string = input("Greeting: ")
    output = value(string)
    print("$",output)

def value(greeting):
    string = greeting.casefold().strip()

    if string.startswith("hello"):
        return 0
    elif string.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()

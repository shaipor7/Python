string = input("Greeting: ")
string = string.casefold().strip()

if string.startswith("hello"):
    print("$0")
elif string.startswith("h"):
    print("$20")
else:
    print("$100")


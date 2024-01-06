import inflect

p = inflect.engine()
list = []
# mylist = p.join(("apple", "banana", "carrot"))

while True:
    try:
        string = input("Name: ")
        list.append(string)
    except EOFError:
        print(p.join(list))
        break

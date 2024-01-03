i = 50
while i>0:
    string = input("Amount Due: ",i)
    if string == 25:
        i -= 25
    elif string == 10:
        i -= 10
    elif string == 5:
        i -= 5
print("Change Owed:",-i)

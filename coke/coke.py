i = 50
while i>0:
    print("Amount Due: ",i)
    string = int(input("Insert coin: "))
    if string == 25 or string == 10 or string == 5:
        i -= string
print("Change Owed:",-i)

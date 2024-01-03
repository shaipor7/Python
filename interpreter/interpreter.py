string = input("Expression: ")

x,y,z = string.split(" ")
x = int(x)
z = int(z)
if y == "+":
    print(float(x+z))
elif y == "-":
    print(float(x-z))
elif y == "*":
    print(float(x*z))
else: print(x/z)


import validators

input = input("What's your email address? ")
if validators.email(input):
    print("Valid")
else:
    print("Invalid")

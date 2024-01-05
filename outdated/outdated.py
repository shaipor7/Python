month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        Input = input("Date: ")
        if Input[0] == int:
            a,b,c = Input.split("/")
        else:
            Input = Input.replace(",", "")
            a,b,c = Input.split(" ")
        break
    except ValueError:
        pass

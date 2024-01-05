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
        if Input[0] == int(Input):
            m,d,y = Input.split("/")
            print(f"{d:02}-{m:02}-{y}")
        else:
            Input = Input.replace(",", "")
            m,d,y = Input.split(" ")
            for i in range(len(month)):
                if m[i] == month:
                    print(f"{d:02}-{i:02}-{y}")
        break
    except ValueError:
        pass

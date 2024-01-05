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
        if Input[0].isdecimal():
            m,d,y = Input.split("/")
            print(f"{y}-{int(m):02}-{int(d):02}")
        else:
            print(Input)
            Input = Input.replace(",", "")
            print(Input)
            m,d,y = Input.split(" ")
            print(m,d,y)
            for i in range(len(month)):
                if m[i] == month:
                    print(f"{y}-{m:02}-{int(d):02}")
        break
    except ValueError:
        pass

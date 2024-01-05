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
        Input = input("Date: ").strip()
        if Input[0].isdecimal():
            m,d,y = Input.split("/")
            if int(m) <= 12 and int(d) <=31:
                print(f"{y}-{int(m):02}-{int(d):02}")
                break
        else:
            # Input = Input.replace(",", "")
            m,d,y = Input.split(" ")
            d = d.split(",")
            if int(d) <=31:
                for i in range(len(month)):
                    if m == month[i]:
                        print(f"{y}-{i+1:02}-{int(d):02}")
                        break
                break
            else:
                pass

    except ValueError:
        pass

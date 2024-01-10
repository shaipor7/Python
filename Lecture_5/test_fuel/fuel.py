def main():
    while True:
        try:
            string = input("Fraction: ")
            x = gauge(convert(string))
            if x == None:
                pass
            else:
                print(x)
                break
        except:
            pass

def convert(fraction):
    list = fraction.split("/")
    integer = round(int(list[0]) / int(list[1]) * 100)
    return integer

def gauge(percentage):
    if percentage > 100:
        pass
    elif 100 >= percentage >= 99:
        return "F"
    elif 1 >= percentage >= 0:
        return "E"
    else:
        return str(percentage) + str("%")


if __name__ == "__main__":
    main()

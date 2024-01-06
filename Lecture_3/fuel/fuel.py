def main():
    x = cal()
    print(x)

def cal():
    while True:
        try:
            string = input("Fraction: ")
            list = string.split("/")
            fraction = int(list[0]) / int(list[1]) * 100
            if fraction > 100:
                pass
            elif 100 >= fraction >= 99:
                return "F"
            elif 1 >= fraction >= 0:
                return "E"
            else:
                return str(round(fraction)) + str("%")
        except (ValueError, ZeroDivisionError):
            pass
main()

def main():
    x = cal()
    print(x)

def cal():
    while True:
        try:
            string = input("Fraction: ")
            list = string.split("/")
            fraction = int(list[0]) / int(list[1])
            if fraction > 1.00:
                pass
            elif 1.00 >= fraction >= 0.99:
                return "F"
            elif fraction >= 0.625:
                return "75%"
            elif 0.625 > fraction >= 0.375:
                return "50%"
            elif 0.375 > fraction > 0.01:
                return "25%"
            else:
                return "E"
        except (ValueError, ZeroDivisionError):
            pass
main()

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
            elif 0.01 >= fraction >= 0.00:
                return "E"
            else:
                return round(fraction) + str("%")
        except (ValueError, ZeroDivisionError):
            pass
main()

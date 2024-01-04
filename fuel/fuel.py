try:
    string = input("Fraction: "))
    list = string.split("/")
    fraction = int(list[0]) / int(list[1])
    if 1.00 >= fraction >= 0.99:
        return "F"
    elif fraction >= 0.75:
        return "75%"
    elif fraction >= 0.50:
        return "50%"
    elif fraction >= 0.25:
        return "25%"
    elif fraction >=
except (ValueError, ZeroDivisionError):


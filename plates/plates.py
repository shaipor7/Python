def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    flag = True
    if s[0:2].isnumeric() or not(2 < len(s) <= 6) :
        flag = False
    else:
        previous = s[0]
        for i in s:
            if (previous.isnumeric() and not(i.isnumeric())) or (previous == '0' and i.isnumeric()) or i in [".", " ", "'"]:
                flag = False
                break
            previous = i
    return flag

main()

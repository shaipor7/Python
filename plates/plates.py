def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    flag = True
    if s[0:2].isnumeric() | not (2 < len(s) <= 6) :
        flag = False
    else:
        for i in s:

                break
    return flag

main()

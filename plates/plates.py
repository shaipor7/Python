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
        for i in range(len(s)):
            if (s[i].isnumeric() and not(s[i+1].isnumeric())) or s[i] in [".", " ", "'"]:
                flag = False
                break
    return flag

main()

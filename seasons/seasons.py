from datetime import date
import sys
import re
import inflect

def convert():
    try:
        input = date.fromisoformat(input("Date of Birth: "))
        now = date.today()
        day = (abs(input - now)).days
    except:
        sys.exit("Invalid date")
    return p.number_to_words(day*24*60, andword="")
    # def __sub__(self):
    #     minutes = self.input -
        # if match := re.search("^(\d{4})-(1[0-2]|0[1-9])-(3[0-1]|[0-2][1-9])$",self.input):
        #     print(match.group(1))
        #     print(match.group(2))
        #     print(match.group(3))
        # else:
        #     sys.exit("Invalid date")


def main():
    a = convert()
    print(a)

if __name__ == "__main__":
    main()

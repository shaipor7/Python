from datetime import date
import sys
import re

class Convert():
    def __init__(self):
        self.input = input("Date of Birth: ")
        print(date.fromisoformat(self.input))
        # if match := re.search("^(\d{4})-(1[0-2]|0[1-9])-(3[0-1]|[0-2][1-9])$",self.input):
        #     print(match.group(1))
        #     print(match.group(2))
        #     print(match.group(3))
        # else:
        #     sys.exit("Invalid date")


def main():
    time = Convert()
    print(time)

if __name__ == "__main__":
    main()

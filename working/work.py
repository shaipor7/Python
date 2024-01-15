import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^([0-9].):?([0-9].) (AM|PM) to ([0-9].):?([0-9].) (AM|PM)$",s):
        if 0 <= int(matches.group(1)) and int(matches.group(2)) <= 12:
            


...


if __name__ == "__main__":
    main()

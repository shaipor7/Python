import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"^([0-9].):?([0-9].) (AM|PM) to $",s)


...


if __name__ == "__main__":
    main()

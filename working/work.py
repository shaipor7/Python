import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.search(r"^(1[0-2]|[1-9])(:([0-5][0-9]))? (AM|PM) to (1[0-2]|[1-9])(:([0-5][0-9]))? (AM|PM)$")
    if not match:
        raise ValueError("Invalid time format")
    else



...


if __name__ == "__main__":
    main()

import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$",ip):
        if i in matches.group() <= 255 and >= 0:
            return True
    else:
        return False

if __name__ == "__main__":
    main()

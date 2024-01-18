import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip):
            if all(0 <= int(i) <= 255 for i in matches.groups()):
                return True
    return False

if __name__ == "__main__":
    main()

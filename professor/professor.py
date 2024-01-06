import random


def main():
    ...


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                generate_integer(level)
        except:
            pass


def generate_integer(level):
    ...


if __name__ == "__main__":
    main()

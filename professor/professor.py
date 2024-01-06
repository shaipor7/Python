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
    for i in range(10):
        x,y = random.randint(1,10*level)
        for i in range(3):
            Input = int(input(f"{x} + {y} = "))
            if Input == (x+y):
                break
            else:
                print("EEE")


if __name__ == "__main__":
    main()

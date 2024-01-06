import random


def main():
    get_level()


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                generate_integer(level)
        except:
            pass


def generate_integer(level):
    score = 0
    for i in range(10):
        x,y = random.randint(1,10*level)
        for i in range(3):
            try:
                Input = int(input(f"{x} + {y} = "))
                if Input == (x+y):
                    score += 1
                    break
                else:
                    print("EEE")
                    if i == 3:
                        print(f"{x} + {y} = {x+y}")
                        
    print("Score: ", score)
if __name__ == "__main__":
    main()

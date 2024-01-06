import random

def main():
    level = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        for i in range(3):
            try:
                Input = int(input(f"{x} + {y} = "))
                if Input == (x+y):
                    score += 1
                    break
                else:
                    print("EEE")
                    if i == 2:
                        print(f"{x} + {y} = {x+y}")
            except ValueError:
                print("EEE")

    print("Score: ", score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                break
        except:
            pass
    return level

def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    else: return random.randint(100,999)

if __name__ == "__main__":
    main()

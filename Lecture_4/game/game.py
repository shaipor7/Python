import random

while True:
    try:
        integer = int(input("Level: "))
        number = random.randint(1,integer)
        while True:
            guess = int(input("Guess: "))
            if guess > number:
                print("Too large!")
            elif guess < number:
                print("Too small!")
            else:
                print("Just right!")
                break
        break
    except:
        pass


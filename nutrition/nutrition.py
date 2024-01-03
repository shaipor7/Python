fruits = {
    "apple":130,
    "avocado":50,
    "banana":110,
    "cantaloupe":50,
    "grapefruit":60,
    "grapes":90,
    "honeydewmelon":50,
    "kiwifruit":90,
    "lemon":15,
    "lime":20,
    "nectarine":60,
    "orange":80,
    "peach":60,
    "pear":100,
    "pineapple":50,
    "plums":70,
    "stawberries":50,
    "sweetcherries":100,
    "tangerine":50,
    "watermelon":80
}
string = input("Item: ").strip().casefold()
for i in fruits:
    if i == string:
        print("Calories:", fruits[i])


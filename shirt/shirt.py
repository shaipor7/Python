import sys
import os
from PIL import Image, ImageOps
try:
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
         sys.exit("Too few command-line arguments")
    else:
        _ , last_1 = os.path.splitext(sys.argv[1])
        _ , last_2 = os.path.splitext(sys.argv[2])
        if last_1 != last_2:
            sys.exit("Input and output have different extensions")
        elif last_1 and last_2 in [".jpg",".png",".jpeg"]:
            shirt = Image.open("shirt.png")
            photo = Image.open(sys.argv[1])
            size = shirt.size
            photo = ImageOps.fit(photo, size)
            photo.paste(shirt, shirt)
            photo.save(sys.argv[2])
        else:
            sys.exit("Invalid input")
except FileNotFoundError:
    sys.exit("File does not exist")

import sys
import os
from PIL import Image, ImageOps
try:
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
         sys.exit("Too few command-line arguments")
    else:
        name , last = os.path.splitext(sys.argv[1])
        if last in [".jpg",".png",".jpeg"]:
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

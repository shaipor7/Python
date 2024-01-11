import sys
import os
count = 0
try:
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
         sys.exit("Too few command-line arguments")
    else:
        name , last = os.path.splitext(sys.argv[1])
        if last in [".jpg",".png",".jpeg"]:
            shirt = Image.open(sys.argv[1])
            size = shirt.size
        else:
            sys.exit("Invalid input")
except FileNotFoundError:
    sys.exit("File does not exist")

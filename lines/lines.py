import sys
data = []
count = 0
try:
    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit
    elif len(sys.argv) < 2:
         print("Too few command-line arguments")
         sys.exit
    else:
        if sys.argv[1].endswith(".py"):
            with open(sys.argv[1]) as file:
                for line in file:
                    if line.startswith("#") or line.lstrip().startswith(""):
                        pass
                    else:
                        count +=1
            print(count)
        else:
            print("Not a Python file")
except FileNotFoundError:
    print("File does not exist")


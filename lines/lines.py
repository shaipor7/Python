import sys
data = []
count = 0
try:
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
         sys.exit("Too few command-line arguments")
    else:
        if sys.argv[1].endswith(".py"):
            with open(sys.argv[1]) as file:
                for line in file:
                    line = line.lstrip().rstrip()
                    if line.startswith("#") or len(line) == 0:
                        pass
                    else:
                        count +=1
            print(count)
        else:
            sys.exit("Not a Python file")
except FileNotFoundError:
    print("File does not exist")


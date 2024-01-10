import sys
data = []
count = 0
try:
    with open(sys.argv[1]) as file:
        for line in file:
            if line.startswith("#") or line.lstrip().startswith(""):
                pass
            else:
                count +=1
except FileNotFoundError:
    print
            data.append(line.rstrip())


import sys
import csv
list = []
try:
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
         sys.exit("Too few command-line arguments")
    else:
        if sys.argv[1].endswith(".csv"):
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    list.append(row)
            print(list)
        else:
            sys.exit("Not a CSV file")
except FileNotFoundError:
    print("File does not exist")

import sys
import csv
from tabulate import tabulate
list = []
try:
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
         sys.exit("Too few command-line arguments")
    else:
        if sys.argv[1].endswith(".csv"):
            with open(sys.argv[1]) as file:
                reader = csv.reader(file)
                for row in reader:
                    list.append(row)
            print(tabulate(list[1:], list[0], tablefmt="grid"))
        else:
            sys.exit("Not a CSV file")
except FileNotFoundError:
    sys.exit("File does not exist")

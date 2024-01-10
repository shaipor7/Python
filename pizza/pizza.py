import sys
import csv
head = []
try:
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
         sys.exit("Too few command-line arguments")
    else:
        if sys.argv[1].endswith(".csv"):
            with open(sys.argv[1]) as file:
                reader = csv.reader(file)
                for topic in reader[0]:
                    head.append(topic)
            print(head)
        else:
            sys.exit("Not a CSV file")
except FileNotFoundError:
    print("File does not exist")

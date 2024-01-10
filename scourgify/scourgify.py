import sys
import csv
lists = []
final_list = []
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
                    lists.append(row)
            for list in lists:
                first, last = list["name"].split(", ")
                list["first"] = first
                list["last"] = last
            for list in lists:
                final_list.append({"first":list["first"], "last":list["last"], "house":list["house"]})
            print(final_list)
        else:
            sys.exit("Not a CSV file")
except FileNotFoundError:
    print("File does not exist")

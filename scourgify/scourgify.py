import sys
import csv
list = []
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
                    list.append(row)
                # for i in list:
                first, last = list[0]["name"].split(", ")
                list[0]["first"] = first
                list[0]["last"] = last
            print(list[0])
            for i in list:
                final_list[i] = {"first":list["first"], "last":list["last"], "house":["house"]}
        else:
            sys.exit("Not a CSV file")
except FileNotFoundError:
    print("File does not exist")

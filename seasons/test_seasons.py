from datetime import date
import sys

class Convert():
    def __init__(self):
        self.input = input("Date of Birth: ")
        if not match := re.search("^([0-9])-()-()$",self.input):
            sys.exit("Invalid date")



def main():
    time = Convert()
    print(time)

if __name__ == "__main__":
    main()

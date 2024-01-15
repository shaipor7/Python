import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert(s):
    matches = re.search(r"^(1[0-2]|[1-9])(:([0-5][0-9]))? (AM|PM) to (1[0-2]|[1-9])(:([0-5][0-9]))? (AM|PM)$",s)
    if not matches:
        raise ValueError("Invalid time format")

    def to_24_hour(hour, minute, meridiem):
        hour, minute = int(hour), int(minute)
        if meridiem == 'PM' and hour != 12:
            hour += 12
        elif meridiem == 'AM' and hour == 12:
            hour = 0
        return f"{hour:02d}:{minute:02d}"

    start_hour = matches.group(1)
    start_minute = matches.group(2)
    start_meridiem = matches.group(3)
    end_hour = matches.group(4)
    end_minute = matches.group(5)
    end_meridiem = matches.group(6)
    start_24 = to_24_hour(start_hour, start_minute, start_meridiem)
    end_24 = to_24_hour(end_hour, end_minute, end_meridiem)

    return f"{start_24} to {end_24}"
if __name__ == "__main__":
    main()

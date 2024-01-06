import sys
import requests

try:
    number = float(sys.argv[1])
except:
    sys.exit("cannot convert to float")

try:
    ...
except requests.RequestException:
    ...

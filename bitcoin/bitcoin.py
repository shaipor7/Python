import sys
import requests
import json

try:
    number = float(sys.argv[1])
except:
    sys.exit("cannot convert to float")

try:
    response = requests.get(" https://api.coindesk.com/v1/bpi/currentprice.json").json()
    print(response["bpi"]["USD"]["rate"])
except requests.RequestException:
    pass

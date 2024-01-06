import sys
import requests
import json

try:
    number = float(sys.argv[1])
except:
    sys.exit("cannot convert to float")

try:
    response = requests.get(" https://api.coindesk.com/v1/bpi/currentprice.json").json()
    print(f"${response["bpi"]["USD"]["rate"]:,.4f}")
except requests.RequestException:
    pass

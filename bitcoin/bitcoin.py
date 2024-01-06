import sys
import requests
import json
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    number = float(sys.argv[1])
except:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get(" https://api.coindesk.com/v1/bpi/currentprice.json").json()
    amount = float(response["bpi"]["USD"]["rate"].replace(",","")) * number
    print(f"${amount:,.4f}")
except requests.RequestException:
    pass

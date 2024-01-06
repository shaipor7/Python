import sys
import requests
import json

try:
    number = float(sys.argv[1])
except:
    sys.exit("Missing command-line argument")

try:
    response = requests.get(" https://api.coindesk.com/v1/bpi/currentprice.json").json()
    amount = float(response["bpi"]["USD"]["rate"].replace(",",""))
    print(f"${amount:,.4f}")
except requests.RequestException:
    pass

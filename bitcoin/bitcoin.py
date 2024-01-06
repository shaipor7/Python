import sys
import requests
import json

try:
    try:
        number = sys.argv[1]
    except:
        sys.exit("Missing command-line argument")
    number = float(number)
except:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get(" https://api.coindesk.com/v1/bpi/currentprice.json").json()
    amount = float(response["bpi"]["USD"]["rate"].replace(",","")) * number
    print(f"${amount:,.4f}")
except requests.RequestException:
    pass

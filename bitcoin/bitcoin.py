import requests
import sys


try:
    if len(sys.argv) < 2:
        sys.exit("Missing Command-Line Arguement")

    number = float(sys.argv[1])
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=46f22e844452348a262e46de41fff2ef2bc9dd728f7487a83773463ffd86834f")
    data = response.json()
    price_usd = float(data["data"]["priceUsd"])

    total_amount = number * price_usd

    print(f"${total_amount:,.4f}")

except ValueError:
    sys.exit("Command is not a number")







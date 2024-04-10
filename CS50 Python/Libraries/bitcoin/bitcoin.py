import requests
import sys
import json

def bitcoin():
    try:
        if len(sys.argv) != 2:
            sys.exit("Missing command-line argument")
        sys.argv[1] = float(sys.argv[1])
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = response.json()
        rate_float = o.get("bpi", {}).get("USD", {}).get("rate_float") #rate_float USD
        return rate_float * sys.argv[1]
    except requests.RequestException:
        bitcoin()
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)


def main():
    result = bitcoin()
    print (f"${result:,.4f}")

if __name__ == "__main__":
    main()

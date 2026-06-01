from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://v6.exchangerate-api.com/"
API_KEY = "YOUR_API_KEY"
printer = PrettyPrinter()

def get_currencies():
    endpoint = f"v6/{API_KEY}/latest/USD"
    url = BASE_URL + endpoint
    data = get(url).json()['conversion_rates']

    data = list(data.items())

    data.sort()
    #printer.pprint(data)
    return data

data = get_currencies()

def print_currencies(currencies):
    for i in currencies:
        name = i[0]
        value = i[1]
        print(f"{name} - {value}")

def exchange_rate(c1,c2,):
    v1 = 0
    v2 = 0
    for i in data:
        name = i[0]
        value = i[1]
        if c1 == name:
            v1 = value
        if c2 == name:
            v2 = value
    c1_to_c2 = v2/v1
    return(c1_to_c2)

def convert(c1,c2,amount):
    return 1.00*amount*(exchange_rate(c1,c2))

def main():
    
    print("Welcome to currency convertor")
    print("List - list the different currencies")
    print("Convert - convert from one currency to another")
    print("Rate - get the exchange rate of two currencies")
    print()

    while True:
        cmd = input("Enter a cmd (q to quit)").lower()
        if cmd == "q":
            break
        elif cmd == "list":
            print_currencies(data)
        elif cmd == "rate":
            c1 = input("Enter a currency name:-").upper()
            c2 = input("Enter a currency name:-").upper()
            print(f"1{c1} = {exchange_rate(c1,c2,)}{c2}")
        elif cmd == "convert":
            c1 = input("Enter a currency name to convert from:-").upper()
            amount = int(input("Enter amount - "))
            c2 = input("Enter a currency name to convert to:-").upper()
            print(f"{amount}{c1} = {convert(c1,c2,amount)}{c2}")
        else:
            print("Invalid cmd")



main()

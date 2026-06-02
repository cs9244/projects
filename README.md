
#Currency Converter

A simple command-line currency converter built with Python. It fetches real-time exchange rates using the ExchangeRate API and allows users to:

View available currencies
Check exchange rates between two currencies
Convert an amount from one currency to another
Features
Real-time exchange rates
Currency listing
Currency-to-currency conversion
Exchange rate lookup
Simple command-line interface
Technologies Used
Python
Requests Library
ExchangeRate API


Installation
Clone the repository:
git clone https://github.com/cs9244/currency-converter.git
Navigate to the project directory:
cd currency-converter
Install dependencies:
pip install requests
Usage

Run the program:

python currency_converter.py

Available commands:

list - Display available currencies

rate - Get the exchange rate between two currencies

convert - Convert an amount from one currency to another

q - Exit the program


Example

Enter a cmd (q to quit): convert
Enter a currency name to convert from: USD
Enter amount: 100
Enter a currency name to convert to: INR

100 USD = 8560 INR
API

This project uses the ExchangeRate API to retrieve live currency exchange rates.

Author

Chinmay

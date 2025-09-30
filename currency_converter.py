import requests

CURRENCY_SYMBOLS = {
    "USD": "$",
    "EUR": "€",
    "GBP": "£",
    "JPY": "¥",
    "NGN": "₦",
    "INR": "₹",
    "CAD": "C$",
    "AUD": "A$",
    "CHF": "CHF",   # Swiss Franc
    "CNY": "¥",    # Chinese Yuan
    "ZAR": "R",    # South African Rand
}


class CurrencyConverter:
    def __init__(self, base_currency="USD"):
        """
        Initialize the converter with a base currency.
        Fetch the latest rates once during initialization.
        """
        self.base_currency = base_currency.upper()
        self.rates = self.get_rates()

    def get_rates(self):
        """
        Fetch exchange rates from the open.er-api.com API.
        Always returns rates relative to USD (default base).
        """
        url = f"https://open.er-api.com/v6/latest/USD"
        response = requests.get(url)

        if response.status_code != 200:
            raise Exception("Error fetching exchange rates")
        
        data = response.json()
        if data["result"] != "success":
            raise Exception (f"API error: {data}")
        
        return data["rates"]
    
    def convert(self, amount, from_currency, to_currency):
        """
        Convert an amount from one currency to another.
        Uses formula: target = amount * (rate_target / rate_source).
        """
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency not in self.rates or to_currency not in self.rates:
            raise ValueError("One of the currencies is not supported.")
        
        rate_source = self.rates[from_currency]
        rate_target = self.rates[to_currency]

        return amount * (rate_target / rate_source)

# Main Program (Interactive)

if __name__ == "__main__":
    converter = CurrencyConverter()

    print("Welcome to the Currency Converter!")
    print("Type 'exit' anytime to quit.\n")

    while True:
        from_curr = input("Enter source currency (e.g, USD, EUR, NGN): ")
        if from_curr.lower() == "exit":
            break

        to_curr = input("Enter target currency: ")
        if to_curr.lower() == "exit":
            break

        try:
            amount = float(input("Enter amount: "))
        except ValueError:
            print("Invalid amount. Try again.\n")
            continue

        try:
            result = converter.convert(amount, from_curr, to_curr)
            
            from_symbol = CURRENCY_SYMBOLS.get(from_curr.upper(), "")
            to_symbol = CURRENCY_SYMBOLS.get(to_curr.upper(), "")


            print(f"{amount:,.2f} {from_symbol} ({from_curr.upper()}) = {result:,.2f} {to_symbol} ({to_curr.upper()})\n")
        except Exception as e:
            print(f"Error: {e}\n")    

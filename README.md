# Project-Currency-Converter

# CURRENCY CONVERTER (PYTHON, OOP)
-   A simple and professional Currency Converter built with Python using Object-Oriented Programming (OOP).
-   It fetches live exchange rates from Exchangerate.host API and allows users to convert between different currencies directly from the terminal.

# FEATURES
- Convert between any two supported currencies (not just from a base currency).
- Fetches real-time exchange rates from the API.
- Handles invalid inputs gracefully with error messages.
- Designed with OOP principles for readability and scalability.
- Clean formatting for conversion results.

# PROJECT STRUCTURE
Project-Currency-Converter/
│── CurrencyConverter.py   # Main Python script
│── README.md              # Project documentation

# INSTALLATION & USAGE
1. Clone the Repository
- `git clone https://github.com/Micheal-jpg/Project-Currency-Converter.git `
- cd currency_converter

2. Install Dependencies
- Make sure you have Python 3 installed.
- install the required library:
pip install requests

3. Run the Program
- python currency_converter.py

4. Example Run
- Enter amount: 100
- From currency (e.g. USD, EUR): usd
- To currency (e.g. NGN, GBP): ngn

- 100 USD = 160000.00 NGN

# TECHNOLOGIES USED
- Python 3
- Requests (for API calls)
- Exchangerate Host API (for live exchange rates)



# HOW IT WORKS
1. The program fetches exchange rates from the API
([ExchangeRate API](https://api.exchangerate.host/latest))

2. The user enters:
- Amount to convert
- Source currency(e.g. USD)
- Target currency(e.g. EUR)

3. The program calculates the conversion using:
- converted = amount x (rate_target / rate_source)

4. The result is displayed with 2 decimal places for clarity

# FUTURE IMPROVEMENTS
- Add a GUI with Tkinter or PyQt for a better user experience
- Add currency symbols ($).
- Add support for historical rates and conversion charts

# AUTHOR
Mike
- GitHub: Micheal-jpg
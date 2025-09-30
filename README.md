# RateWise

## CURRENCY CONVERTER (PYTHON, OOP)
-   A simple and professional Currency Converter built with Python using Object-Oriented Programming (OOP).
-   It fetches live exchange rates from Exchangerate.host API and allows users to convert between different currencies directly from the terminal.
-   Now updated with **currency symbols** (e.g., `$`, `€`, `₦`) for a more user-friendly experience.  


## FEATURES
- Convert between any two supported currencies (not just from a base currency).
- Fetches real-time exchange rates from the API.
- Handles invalid inputs gracefully with error messages.
- Designed with OOP principles for readability and scalability.
- Clean formatting for conversion results.
- Displays results with currency symbols for better readability.
- Supports multiple currencies.

## PROJECT STRUCTURE
```bash
PROJECT-CURRENCY-CONVERTER/
│── currency_converter.py  # Main Python program
│── README.md              # Project documentation
```          

## INSTALLATION & USAGE
1. Clone the Repository
```bash
git clone https://github.com/Micheal-jpg/Project-Currency-Converter.git 
cd Project-Currency-Converter
```

2. Install Dependencies
```bash
Make sure you have Python 3 installed, then install the required library:
pip install requests
```

3. Run the Program
```bash
python currency_converter.py
```
Example Run
```bash
Enter amount: 50
From currency (e.g. USD, EUR): usd
To currency (e.g. NGN, GBP): ngn

100 $ (USD) = 160000.00 ₦ (NGN)
```

## TECHNOLOGIES USED
- Python 3
- Requests (for API calls)
- Exchangerate Host API (for live exchange rates)



## HOW IT WORKS
1. The program fetches exchange rates from the API
([Exchangerate.host API](https://open.er-api.com/v6/latest/USD))

2. The user enters:
- Amount to convert
- Source currency(e.g. USD, NGN, EUR)
- Target currency(e.g. EUR, AUD, GBP)

3. The program calculates the conversion using:
```bash
converted = amount x (rate_target / rate_source)
```

4. The result is displayed with 2 decimal places for clarity

## FUTURE IMPROVEMENTS
- Add a GUI with Tkinter or PyQt for a better user experience
- Add support for historical rates and conversion charts


**AUTHOR:** Mike
- [GitHub Profile](https://github.com/Micheal-jpg)
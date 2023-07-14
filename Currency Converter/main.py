import pyttsx3
from forex_python.converter import CurrencyRates


def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    result = c.convert(from_currency, to_currency, amount)
    return result


def currency_converter():
    engine = pyttsx3.init()
    engine.say("OK, do you want to see the currency code list, if yes, just press y and, if not then,"
               " press any key")
    engine.runAndWait()

    option = str(input("Do you want to see the currency code list, if yes, just press y and if not then,"
                       " press any key = "))

    if option == 'y' or option == 'Y':
        engine = pyttsx3.init()
        engine.say("OK, here I am sharing all the currency codes with you.")
        engine.runAndWait()

        # Display the currency codes before running the currency converter
        display_currency_codes()

    else:
        engine = pyttsx3.init()
        engine.say("So, you don't want me to display the list, no worries !")
        engine.runAndWait()

    engine = pyttsx3.init()
    engine.say("Enter the amount to convert")
    engine.runAndWait()

    amount = float(input("Enter the amount to convert: "))

    engine = pyttsx3.init()
    engine.say("Ok, you have entered an amount of {:.2f}".format(amount))
    engine.runAndWait()

    engine = pyttsx3.init()
    engine.say("Enter the currency to convert from")
    engine.runAndWait()

    from_currency = input("Enter the currency to convert from: ").upper()

    engine = pyttsx3.init()
    engine.say("Enter the currency to convert to")
    engine.runAndWait()

    to_currency = input("Enter the currency to convert to: ").upper()

    engine = pyttsx3.init()
    engine.say("Sweetheart, I am converting, please wait for 1 second")
    engine.runAndWait()

    converted_amount = convert_currency(amount, from_currency, to_currency)

    engine = pyttsx3.init()
    engine.say("So the converted amount and detailed summary is given below "
               "= {:.2f}".format(converted_amount))
    engine.runAndWait()

    print(f"{amount} {from_currency} = {converted_amount} {to_currency}")


def display_currency_codes():
    currency_names = {
        "AED": "United Arab Emirates Dirham",
        "AFN": "Afghan Afghani",
        "ALL": "Albanian Lek",
        "AMD": "Armenian Dram",
        "ANG": "Netherlands Antillean Guilder",
        "AOA": "Angolan Kwanza",
        "ARS": "Argentine Peso",
        "AUD": "Australian Dollar",
        "AWG": "Aruban Florin",
        "AZN": "Azerbaijani Manat",
        "BAM": "Bosnia-Herzegovina Convertible Mark",
        "BBD": "Barbadian Dollar",
        "BDT": "Bangladeshi Taka",
        "BGN": "Bulgarian Lev",
        "BHD": "Bahraini Dinar",
        "BIF": "Burundian Franc",
        "BMD": "Bermudan Dollar",
        "BND": "Brunei Dollar",
        "BOB": "Bolivian Boliviano",
        "BRL": "Brazilian Real",
        "BSD": "Bahamian Dollar",
        "BTC": "Bitcoin",
        "BTN": "Bhutanese Ngultrum",
        "BWP": "Botswanan Pula",
        "BYN": "Belarusian Ruble",
        "BZD": "Belize Dollar",
        "CAD": "Canadian Dollar",
        "CDF": "Congolese Franc",
        "CHF": "Swiss Franc",
        "CLF": "Chilean Unit of Account (UF)",
        "CLP": "Chilean Peso",
        "CNH": "Chinese Yuan (Offshore)",
        "CNY": "Chinese Yuan",
        "COP": "Colombian Peso",
        "CRC": "Costa Rican Colón",
        "CUC": "Cuban Convertible Peso",
        "CUP": "Cuban Peso",
        "CVE": "Cape Verdean Escudo",
        "CZK": "Czech Republic Koruna",
        "DJF": "Djiboutian Franc",
        "DKK": "Danish Krone",
        "DOP": "Dominican Peso",
        "DZD": "Algerian Dinar",
        "EGP": "Egyptian Pound",
        "ERN": "Eritrean Nakfa",
        "ETB": "Ethiopian Birr",
        "EUR": "Euro",
        "FJD": "Fijian Dollar",
        "FKP": "Falkland Islands Pound",
        "GBP": "British Pound Sterling",
        "GEL": "Georgian Lari",
        "GGP": "Guernsey Pound",
        "GHS": "Ghanaian Cedi",
        "GIP": "Gibraltar Pound",
        "GMD": "Gambian Dalasi",
        "GNF": "Guinean Franc",
        "GTQ": "Guatemalan Quetzal",
        "GYD": "Guyanaese Dollar",
        "HKD": "Hong Kong Dollar",
        "HNL": "Honduran Lempira",
        "HRK": "Croatian Kuna",
        "HTG": "Haitian Gourde",
        "HUF": "Hungarian Forint",
        "IDR": "Indonesian Rupiah",
        "ILS": "Israeli New Shekel",
        "IMP": "Manx pound",
        "INR": "Indian Rupee",
        "IQD": "Iraqi Dinar",
        "IRR": "Iranian Rial",
        "ISK": "Icelandic Króna",
        "JEP": "Jersey Pound",
        "JMD": "Jamaican Dollar",
        "JOD": "Jordanian Dinar",
        "JPY": "Japanese Yen",
        "KES": "Kenyan Shilling",
        "KGS": "Kyrgystani Som",
        "KHR": "Cambodian Riel",
        "KMF": "Comorian Franc",
        "KPW": "North Korean Won",
        "KRW": "South Korean Won",
        "KWD": "Kuwaiti Dinar",
        "KYD": "Cayman Islands Dollar",
        "KZT": "Kazakhstani Tenge",
        "LAK": "Laotian Kip",
        "LBP": "Lebanese Pound",
        "LKR": "Sri Lankan Rupee",
        "LRD": "Liberian Dollar",
        "LSL": "Lesotho Loti",
        "LYD": "Libyan Dinar",
        "MAD": "Moroccan Dirham",
        "MDL": "Moldovan Leu",
        "MGA": "Malagasy Ariary",
        "MKD": "Macedonian Denar",
        "MMK": "Myanmar Kyat",
        "MNT": "Mongolian Tugrik",
        "MOP": "Macanese Pataca",
        "MRO": "Mauritanian Ouguiya (pre-2018)",
        "MRU": "Mauritanian Ouguiya",
        "MUR": "Mauritian Rupee",
        "MVR": "Maldivian Rufiyaa",
        "MWK": "Malawian Kwacha",
        "MXN": "Mexican Peso",
        "MYR": "Malaysian Ringgit",
        "MZN": "Mozambican Metical",
        "NAD": "Namibian Dollar",
        "NGN": "Nigerian Naira",
        "NIO": "Nicaraguan Córdoba",
        "NOK": "Norwegian Krone",
        "NPR": "Nepalese Rupee",
        "NZD": "New Zealand Dollar",
        "OMR": "Omani Rial",
        "PAB": "Panamanian Balboa",
        "PEN": "Peruvian Sol",
        "PGK": "Papua New Guinean Kina",
        "PHP": "Philippine Peso",
        "PKR": "Pakistani Rupee",
        "PLN": "Polish Złoty",
        "PYG": "Paraguayan Guarani",
        "QAR": "Qatari Rial",
        "RON": "Romanian Leu",
        "RSD": "Serbian Dinar",
        "RUB": "Russian Ruble",
        "RWF": "Rwandan Franc",
        "SAR": "Saudi Riyal",
        "SBD": "Solomon Islands Dollar",
        "SCR": "Seychellois Rupee",
        "SDG": "Sudanese Pound",
        "SEK": "Swedish Krona",
        "SGD": "Singapore Dollar",
        "SHP": "Saint Helena Pound",
        "SLL": "Sierra Leonean Leone",
        "SOS": "Somali Shilling",
        "SRD": "Surinamese Dollar",
        "SSP": "South Sudanese Pound",
        "STD": "São Tomé and Príncipe Dobra (pre-2018)",
        "STN": "São Tomé and Príncipe Dobra",
        "SVC": "Salvadoran Colón",
        "SYP": "Syrian Pound",
        "SZL": "Swazi Lilangeni",
        "THB": "Thai Baht",
        "TJS": "Tajikistani Somoni",
        "TMT": "Turkmenistani Manat",
        "TND": "Tunisian Dinar",
        "TOP": "Tongan Pa'anga",
        "TRY": "Turkish Lira",
        "TTD": "Trinidad and Tobago Dollar",
        "TWD": "New Taiwan Dollar",
        "TZS": "Tanzanian Shilling",
        "UAH": "Ukrainian Hryvnia",
        "UGX": "Ugandan Shilling",
        "USD": "United States Dollar",
        "UYU": "Uruguayan Peso",
        "UZS": "Uzbekistan Som",
        "VEF": "Venezuelan Bolívar (pre-2018)",
        "VES": "Venezuelan Bolívar",
        "VND": "Vietnamese Dong",
        "VUV": "Vanuatu Vatu",
        "WST": "Samoan Tala",
        "XAF": "CFA Franc BEAC",
        "XAG": "Silver Ounce",
        "XAU": "Gold Ounce",
        "XCD": "East Caribbean Dollar",
        "XDR": "Special Drawing Rights",
        "XOF": "CFA Franc BCEAO",
        "XPD": "Palladium Ounce",
        "XPF": "CFP Franc",
        "XPT": "Platinum Ounce",
        "YER": "Yemeni Rial",
        "ZAR": "South African Rand",
        "ZMW": "Zambian Kwacha",
        "ZWL": "Zimbabwean Dollar"
    }
    print("\n")

    print("Currency Codes and Names:")
    for code, name in currency_names.items():
        print(f"{code}: {name}")

    print("\n")


def main_function():
    print("\n")
    print("     **** Welcome to the Currency Converting Software ****")
    print("                (Developed by Talha Khalid)")
    print("\n")
    print("In my system, Mr. Talha Khalid, the developer of this software,"
          " has used built-in libraries such as pyttsx3 and CurrencyRates.\n"
          "Forget about the internet connection problems, just open my software,"
          " give me the amount you want to convert from one currency\nto another"
          " currency in just one step you will get the solutions to your problems.")

    # Text-To-Speech code
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Index 1 represents a female voice

    engine.say("Welcome to the Currency Converting Software. Developed by Talha Khalid")
    engine.say("In my system, Mr. Talha Khalid, the developer of this software,"
               " has used built-in libraries such as pyttsx3 and CurrencyRates."
               " Forget about the internet connection problems, just open me by one click,"
               " give me the amount, you want to convert from one currency to another"
               "currency, and in just one step you will get the solutions to your problems.....")
    engine.runAndWait()

    while 1:
        currency_converter()

        engine = pyttsx3.init()
        engine.say("Dear user, do you want to use me again?"
                   " If yes, press y, and if no, press any key...")
        engine.runAndWait()

        option_2 = str(input("Dear user, do you want to use me again?\n"
                             "If yes, press y, and if no, press any key: "))

        if option_2.lower() != 'y':
            break

    engine = pyttsx3.init()
    engine.say("Thank you so much, respected user for using me. Thanks once again, have a lovely day. Bye bye!")
    engine.runAndWait()


main_function()


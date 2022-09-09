# Unicode

# How to write a euro sign can be found at Currency Symbols. How to write emoji can be found at emoji, you can also check the formal charts for symbols you use either name or code: \N{money-mouth face}, or code \U0001F911

# Write a program that fulfills the specification

# Let the user input a price, i.e Your new car cost: 1000000
# Add a currency symbol (not dollar) to the input string. ie. Your new car cost [$]
# Depending on the price, respond with a matching emoji (you decide which ones) i.e if cost below 50000 use one emoji, if is above another one


from platform import python_branch


price = input('Write a price for yout new car: \u20AC')
print(f'You new car cost: \u20AC{price}')
if price <= "5000":
    print('\N{grinning face}');
else:
    print('\N{worried face}')

# Currency in python

"""
EUR = u20AC
USD = u0024

u00A2	CENT SIGN	¢	
u00A3	POUND SIGN	£	
u00A4	CURRENCY SIGN	¤	
u00A5	YEN SIGN	¥	
u058F	ARMENIAN DRAM SIGN	֏	
u060B	AFGHANI SIGN	؋	
u07FE	NKO DOROME SIGN	߾	
u07FF	NKO TAMAN SIGN	߿	
u09F2	BENGALI RUPEE MARK	৲	
u09F3	BENGALI RUPEE SIGN	৳	
u09FB	BENGALI GANDA MARK	৻	
u0AF1	GUJARATI RUPEE SIGN	૱	
u0BF9	TAMIL RUPEE SIGN	௹	
u0E3F	THAI CURRENCY SYMBOL BAHT	฿	
u17DB	KHMER CURRENCY SYMBOL RIEL	៛	
u20A0	EURO-CURRENCY SIGN	₠	
u20A1	COLON SIGN	₡	
u20A2	CRUZEIRO SIGN	₢	
u20A3	FRENCH FRANC SIGN	₣	
u20A4	LIRA SIGN	₤	
u20A5	MILL SIGN	₥	
u20A6	NAIRA SIGN	₦	
u20A7	PESETA SIGN	₧	
u20A8	RUPEE SIGN	₨	
u20A9	WON SIGN	₩	
u20AA	NEW SHEQEL SIGN	₪	
u20AB	DONG SIGN	₫	
u20AC	EURO SIGN	€	
u20AD	KIP SIGN	₭	
u20AE	TUGRIK SIGN	₮	
u20AF	DRACHMA SIGN	₯	
u20B0	GERMAN PENNY SIGN	₰	
u20B1	PESO SIGN	₱	
u20B2	GUARANI SIGN	₲	
u20B3	AUSTRAL SIGN	₳	
u20B4	HRYVNIA SIGN	₴	
u20B5	CEDI SIGN	₵	
u20B6	LIVRE TOURNOIS SIGN	₶	
u20B7	SPESMILO SIGN	₷	
u20B8	TENGE SIGN	₸	
u20B9	INDIAN RUPEE SIGN	₹	
u20BA	TURKISH LIRA SIGN	₺	
u20BB	NORDIC MARK SIGN	₻	
u20BC	MANAT SIGN	₼
u20BD	RUBLE SIGN	₽	
u20BE	LARI SIGN	₾	
u20BF	BITCOIN SIGN	₿	
u20C0	SOM SIGN	⃀	
uA838	NORTH INDIC RUPEE MARK	꠸	
uFDFC	RIAL SIGN	﷼	
uFE69	SMALL DOLLAR SIGN	﹩	
uFF04	FULLWIDTH DOLLAR SIGN	＄	
uFFE0	FULLWIDTH CENT SIGN	￠	
uFFE1	FULLWIDTH POUND SIGN	￡	
uFFE5	FULLWIDTH YEN SIGN	￥	
uFFE6	FULLWIDTH WON SIGN	￦	
u11FDD	TAMIL SIGN KAACU	𑿝	
u11FDE	TAMIL SIGN PANAM	𑿞	
u11FDF	TAMIL SIGN PON	𑿟	
u11FE0	TAMIL SIGN VARAAKAN	𑿠	
u1E2FF	WANCHO NGUN SIGN	𞋿	
u1ECB0	INDIC SIYAQ RUPEE MARK
 """
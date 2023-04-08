from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes

CURRENCY_RATES = CurrencyRates(force_decimal=True)
CURRENCY_CODES = CurrencyCodes()


class Currency():

    def __init__(self, val, final, amount):
        self.val = val
        self.final = final
        self.amount = amount

    def convert_amount(self, val, final, amount):
        """ pass amount and convert curency """ 
        
        c = CurrencyRates()
        convert = c.convert(val, final , amount)

        return convert

    def curr_symbol(self, final):
        """get the symbol for the converted currency ."""

        symbol = CURRENCY_CODES.get_symbol(final)

        return symbol
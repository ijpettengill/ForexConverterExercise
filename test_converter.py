from unittest import TestCase

from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes
from converter import Currency

from app import app

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

class TestCurrency(TestCase):
     """Tests for Currency class and the methods within it."""

     def setUp(self):
        """Method that runs before every test method."""

        first = Currency('USD','USD',1)
        

     def test_convert_amount(self):
        """Test for convert_amount() method in Currency class."""

        first = 'USD'
        final = 'USD'
        amount = 1
        c = CurrencyRates()
        curr_conversion = c.convert(first, final, amount)
        self.assertNotEqual(curr_conversion, 2)
        self.assertEqual(curr_conversion, 1)

     def test_currency_symbol(self):
        """Test for currency_symbol() method in Currency class."""

        init = 'USD'
        c2 = CurrencyCodes()
        c_symbol = c2.get_symbol(init)
        self.assertEqual(c_symbol, 'US$')
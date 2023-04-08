from unittest import TestCase
from converter import Currency
from app import app


app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class TestRoutes(TestCase):

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True
        app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


    def test_landing_page(self):
        """Tests the GET and POST routes for the form on landing page."""
        
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)

    def test_calculate_conversion(self):
        """Tests the routes for conversion calculation."""
        
        with app.test_client() as client:
            resp = client.post('/results', data={'first': 'USD', 'final': 'USD', 'amount': 1})
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('1', html)

            resp = client.post('/results', data={'first': 'qqq', 'final': 'USD', 'amount': 1})
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.location, 'http://localhost/')

            resp = client.post('/results', data={'first': 'USD', 'final': 'qqq', 'amount': 1})
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.location, 'http://localhost/')

            resp = client.post('/results', data={'first': 'USD', 'final': 'USD', 'amount': 'qqq'})
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.location, 'http://localhost/')            


    def test_redirect_followed(self):
        """Tests redirects for wrong form inputs."""
        
        with app.test_client() as client:
            resp = client.post('/results', follow_redirects=True, 
                data={'first': 'qqq', 'final': 'USD', 'amount': 1})
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<strong>Please enter a valid currency</strong>', html)

            resp = client.post('/results', follow_redirects=True, 
                data={'first': 'USD', 'final': 'qqq', 'amount': 1})
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<strong>Please enter a valid currency</strong>', html)